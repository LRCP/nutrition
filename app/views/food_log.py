import json
import copy
from collections import defaultdict

from flask import redirect, url_for, render_template, request
from flask.ext.login import login_required, current_user

from app import app, session, ordered_defaultdict
from app.models.food_log import FoodLog
from app.models.food_log_food_association import FoodLogFoodAssociation
from app.models.user_food_group_association import UserFoodGroupAssociation
from app.models.usda import FoodDescription, FoodGroupDescription, Weight
from app.models.usda import NutrientData
from app.constants import food_nutrient_dictionary

def get_food_log(user):
    food_log = session.query(FoodLog).filter_by(user=user).first()
    if food_log is None:
        food_log = FoodLog()
        food_log.user = user
        session.add(food_log)

        session.commit()
    return food_log


def sum_nutrients(nutrient_keys, nutrient_dictionary):
    total = 0
    for key in nutrient_keys:
        if nutrient_dictionary[key] == "N/A":
            continue
        total = total + nutrient_dictionary[key]
    return total


@app.route('/food_log', methods=['GET'])
@login_required
def food_log_get():
    user = current_user

    # Hack: If the user has no protein goal they have no profile!
    if user.protein_goal == None:
        return redirect(url_for('profile_get'))

    # Get a list of all of the food groups
    all_food_groups = session.query(FoodGroupDescription)
    #order_by orders the food groups alphabetically according to the description
    all_food_groups = all_food_groups.order_by(FoodGroupDescription.FdGrp_Desc)
    all_food_groups = all_food_groups.all()
    food_groups = []
    for food_group in all_food_groups:
        for selected_food_group in user.selected_food_groups:
            if food_group.FdGrp_Cd == selected_food_group.food_group_code:
                food_groups.append((food_group, True))
                break 
        else:
            food_groups.append((food_group, False))  
    #for food_group in user.selected_food_groups:





    # Get the current food log
    food_log = get_food_log(user)

    # Build a list of foods with their nutrients etc.
    foods = []
    for association in food_log.foods:
        ndb = association.food_NDB_No
        seq = association.unit_Seq

        food = session.query(FoodDescription).get(ndb)
        unit = session.query(Weight).filter_by(NDB_No=ndb, Seq=seq).first()

        nutrients = session.query(NutrientData).filter_by(NDB_No=ndb).all()
        units = session.query(Weight).filter_by(NDB_No=ndb).all()


        nutrient_dict = copy.deepcopy(food_nutrient_dictionary)
        for category_name, category in food_nutrient_dictionary.iteritems():
            for nutrient_name, nutrient_number in category.iteritems():
                nutrient_number = str(nutrient_number)
                try:
                    value = next(x.Nutr_Val for x in nutrients
                                 if x.Nutr_No == nutrient_number)
                    value = (float(value) * association.quantity *
                             float(unit.Gm_Wgt) / 100)
                except StopIteration:
                    value = "N/A"
                nutrient_dict[category_name][nutrient_name] = value

        # Post-process the list to add some extra nutrients
        ffa = nutrient_dict["Fats & Fatty Acids"]
        omega_3_keys = [
            "18:3 n-3 c,c,c (ALA) alpha-linolenic",
            "20:3 n-3 eicosatrienoic acid (ETE)",
            "20:4 undifferentiated arachidonic",
            "20:5 n-3 (EPA) eicosapentaenoic timnodonic",
            "22:5 n-3 (DPA) docosapentaenoic acid",
            "22:6 n-3 (DHA)"
            ]

        ffa["omega_3"] = sum_nutrients(omega_3_keys, ffa)

        omega_6_keys = [
            "18:2 n-6 c,c Linoleic acid (LA)",
            "18:3 n-6 c,c,c (GLA) gamma-linolenic acid ",
            "20:2 n-6 c,c eicosadienoic acid",
            "20:3 n-6 (DGLA) dihomo-gamma-linolenic acid",
            "20:4 n-6 (AA) arachidonic acid"
        ]

        ffa["omega_6"] = sum_nutrients(omega_6_keys, ffa)

        foods.append({
            "name": food.Long_Desc,
            "id": association.id,
            "quantities": association.quantity,
            "nutrients": nutrient_dict,
            "unit": unit.Msre_Desc,
        })


    # Total the number of nutrients consumed
    totals = defaultdict(lambda: ordered_defaultdict.OrderedDefaultdict(float))
    for food in foods:
        nutrients = food["nutrients"]
        for category_name, category in nutrients.iteritems():
            for nutrient_name, nutrient_value in category.iteritems():
                if nutrient_value == "N/A":
                    continue
                totals[category_name][nutrient_name] += nutrient_value

    foods.append({
        "name": "Totals",
        "nutrients": totals,
    })

    return render_template(
        'food_log.html', title="FoodLog",
        food_nutrient_list=foods,
        food_groups_list=food_groups,
        user=user
    )


@app.route('/food_log', methods=['POST'])
@login_required
def food_log_post():
    user = current_user

    quantity = request.form.get('quantity')
    unit = request.form.get('unit')
    unit = json.loads(unit)

    food_log = get_food_log(user)

    association = FoodLogFoodAssociation(
        food_NDB_No=unit["NDB_No"],
        unit_Seq=unit["Seq"],
        quantity=float(quantity)
    )

    food_log.foods.append(association)

    session.commit()
    return redirect(url_for('food_log_get'))

@app.route('/food_log/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete_food(id):
    association = session.query(Association).get(id)
    session.delete(association)
    return redirect(url_for('food_log_get'))

@app.route('/food_log/selected_food_groups', methods=['GET', 'POST'])
@login_required
def selected_food_groups():
    user = current_user

    # Get and parse a comma-seperated query string
    food_groups = request.args.get('food_groups')
    if food_groups == None:
        return ""
    food_groups = food_groups.split(',')

    user.selected_food_groups = []
    for code in food_groups:
        association = UserFoodGroupAssociation(
            food_group_code=code
        )
        user.selected_food_groups.append(association)

    session.commit()
    return ""




