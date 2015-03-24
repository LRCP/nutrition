import json
import copy
from collections import defaultdict, OrderedDict

from flask import redirect, url_for, render_template, request
from flask.ext.login import login_required, current_user

from app import app, session, ordered_defaultdict
from app.models.food_log import FoodLog
from app.models.food_log_food_association import FoodLogFoodAssociation
from app.models.user_food_group_association import UserFoodGroupAssociation
from app.models.usda import FoodDescription, FoodGroupDescription, Weight, NutrientDefinition
from app.models.usda import NutrientData
from app.constants import food_nutrient_dictionary_new
#from app.constants import food_nutrient_dictionary
from app.models.favorite_association import FavoriteAssociation

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

def nutrient_number_to_quantity(nutrients, nutrient_number, association, unit):
    #consider passing quantity and weight instead of association and unit.
    try:
        value = next(x.Nutr_Val for x in nutrients
            if x.Nutr_No == nutrient_number)
        value = (float(value) * association.quantity *
            float(unit.Gm_Wgt) / 100)
    except StopIteration:
        value = "N/A"     
            #puts the value into the nutrient_dict
    #nutrient_dict[category_name][nutrient_name] = value. replace by return value.
    return value
   



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



    nutrient_definitions = session.query(NutrientDefinition).all()
    print nutrient_definitions[0].NutrDesc


    # Get the current food log
    food_log = get_food_log(user)

    # Build a list of foods with their nutrients etc.
    foods = []
    for association in food_log.foods:
        ndb = association.food_NDB_No
        seq = association.unit_Seq

        food = session.query(FoodDescription).get(ndb)
        unit = session.query(Weight).filter_by(NDB_No=ndb, Seq=seq).first()

        #get all the nutrient's data by serching by its ndb.no
        nutrients = session.query(NutrientData).filter_by(NDB_No=ndb).all()
        units = session.query(Weight).filter_by(NDB_No=ndb).all()

       
        nutrient_dict = copy.deepcopy(food_nutrient_dictionary_new)
        #nutrient_dict contains a category_name mapped to a dictionary
        #containing the nutrient_numbers.
        for category_name, category in food_nutrient_dictionary_new.iteritems():
            
            
                #the category, which is a dictionary maps the name of a nutrient to 
                #a tuple that contains the nutrient_number plus a dictionary of 
                #subnutrients.
            category = food_nutrient_dictionary_new[category_name]
            
          
            for nutrient_name, nutrient_tuple in category.iteritems():
                nutrient_number = nutrient_tuple[0]
                if nutrient_number != None:
                    value = nutrient_number_to_quantity(
                        nutrients, str(nutrient_number), association, unit
                        )
                    
                    # lambda function finds the matching nutrient_definition in the nutr_def table
                    # filtering by nutrient number. It will return the information in the form of a list.
                    
                    nutrient_definition = filter(
                        lambda nutrient_definition: 
                           nutrient_definition.Nutr_No == str(nutrient_number), 
                        nutrient_definitions)[0]
                    nutrient_unit = nutrient_definition.Units
                    unit_precision = nutrient_definition.Num_Dec
                    if isinstance(value, float):
                        value = round(value, int(unit_precision))

                else:
                    value = ""
                    nutrient_unit = ""
                    

                
                
                
                #puts the value into the nutrient_dict
                nutrient_dict[category_name][nutrient_name] = (value, OrderedDict(), nutrient_unit)
                
                #loop throught the subnutrients to get the name and number.
                for subnutrient_name, subnutrient_number in nutrient_tuple[1].iteritems():
                    if subnutrient_number != None:
                        value = nutrient_number_to_quantity(
                            nutrients, str(subnutrient_number), association, unit
                            )
                        subnutrient_definition = filter(
                            lambda subnutrient_definition: 
                                subnutrient_definition.Nutr_No == str(subnutrient_number), 
                            nutrient_definitions)[0]
                    subnutrient_unit = subnutrient_definition.Units
                    unit_precision = subnutrient_definition.Num_Dec
                    if isinstance(value, float):
                        value = round(value, int(unit_precision))

                else:
                    value = ""
                    subnutrient_unit = ""
                    



                    if subnutrient_number == 318:
                        print value


                    
                    # to access the value of OrderedDict
                    nutrient_dict[category_name][nutrient_name][1][subnutrient_name] = value

                   

            

        # Post-process the list to add some extra nutrients
        # ffa = nutrient_dict["Fats & Fatty Acids"]
        # omega_3_keys_ALA = [
        #     "18:3 n-3 cis,cis,cis (ALA)  linolenic alpha-linolenic"
        #     ]
        #     #"20:3 n-3 eicosatrienoic acid (ETE)",
        #     #"20:4 undifferentiated arachidonic",
        # omega_3_keys_EPA_DHA = [
        #     "20:5 n-3 eicosapentaenoic (EPA)  timnodonic",
        #     #"22:5 n-3 docosapentaenoic (DPA)  clupanodonic",
        #     "22:6 n-3 docosahexaenoic (DHA)  cervonic"
        #     ]

        # ffa["omega_3_ALA"] = sum_nutrients(omega_3_keys_ALA, ffa)
        # ffa["omega_3_keys_EPA_DHA"] = sum_nutrients(omega_3_keys_EPA_DHA, ffa)

        # omega_6_keys = [
        #     "18:2 n-6 cis,cis (LA)  linoleic",
        #     "18:3 n-6 cis,cis,cis (GLA)  gamma-linolenic",
        #     #"20:2 n-6 cis,cis eicosadienoic",
        #     #"20:3 n-6 (DGLA) dihomo-gamma-linolenic acid",
        #     "20:4 n-6 eicosatetraenoic (AA)  arachidonic"
        # ]

        

        # ffa["omega_6"] = sum_nutrients(omega_6_keys, ffa)

        foods.append({
            "name": food.Long_Desc,
            "id": association.id,
            "quantity": association.quantity,
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
                #totals[category_name][nutrient_name] += nutrient_value

    foods.append({
        "name": "Totals",
        "nutrients": totals,
    })
    calorie_percentage = (
        totals["Calorie Information"]["Energy_KCAL"] *100
        )
    calorie_percentage /= user.get_adjusted_daily_caloric_needs()

    protein_percentage = (
        totals["Protein & Amino Acids"]["Protein"] * 100
        )
    protein_percentage /= user.get_adjusted_daily_caloric_needs()

    carbohydrate_percentage = (
        totals["Carbohydrates"]["Carbohydrate, by difference"] * 100
        )
    carbohydrate_percentage /= user.get_adjusted_daily_caloric_needs()
    fat_percentage = (
        totals["Fats & Fatty Acids"]["Total lipid (fat)"] * 100
        )
    fat_percentage /= user.get_adjusted_daily_caloric_needs()

    
    return render_template(
        'food_log.html', title="FoodLog",
        food_nutrient_list=foods,
        food_groups_list=food_groups,
        user=user,
        calorie_percentage=calorie_percentage,
        protein_percentage=protein_percentage,
        carbohydrate_percentage=carbohydrate_percentage,
        fat_percentage=fat_percentage,
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

    #build the query
    favorite_query = session.query(FavoriteAssociation)
    favorite_query = favorite_query.filter_by(NDB_No=unit["NDB_No"], user_id=user.id)
    #executing the query
    favorite = favorite_query.first()

    if favorite == None:
        favorite = FavoriteAssociation(
            NDB_No=unit["NDB_No"],
            user_id=user.id,
            popularity=1
        )
        session.add(favorite)
    else:
        favorite.popularity += 1
    session.commit()
    return redirect(url_for('food_log_get'))

@app.route('/food_log/delete/<id>', methods=['GET', 'POST'])

@login_required
def delete_food(id):
    association = session.query(FoodLogFoodAssociation).get(id)
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




