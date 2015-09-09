# coding=utf-8
import json
import copy
from collections import defaultdict, OrderedDict

from flask import flash, redirect, url_for, render_template, request
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
from app.models.meal import Meal
from app.models.meal_food_association import MealFoodAssociation

def build_food_list(input_foods, nutrient_definitions):
    # Build a list of foods with their nutrients etc.
    foods = []

    for association in input_foods:
        ndb = association.food_NDB_No
        seq = association.unit_Seq
        food = session.query(FoodDescription).get(ndb)
        unit = session.query(Weight).filter_by(NDB_No=ndb, Seq=seq).first()
        #get all the nutrient's data by serching by its ndb.no
        nutrients = session.query(NutrientData).filter_by(NDB_No=ndb).all()
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

                    # unpack the tuple that returns nutrient_unit when 
                    # the arguments nutrient_definitions and nutrient are passed into the get_nutrient_unit function.
                    nutrient_unit, unit_precision = get_nutrient_unit(nutrient_definitions, nutrient_number)
                    # unpack the tuple that returns the value and nutrient_unit when
                    # the arguments value, nutrient_unit and unit_precision are passed into the format_unit_for_display function.
                    value, nutrient_unit = format_unit_for_display(value, nutrient_unit, unit_precision)                    
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
                        subnutrient_unit, unit_precision = get_nutrient_unit(nutrient_definitions, subnutrient_number)
                        value, subnutrient_unit = format_unit_for_display(value, subnutrient_unit, unit_precision)
                    else:
                        value = ""
                        subnutrient_unit = ""
                    
                    # to access the value of OrderedDict
                    nutrient_dict[category_name][nutrient_name][1][subnutrient_name] = (value, subnutrient_unit)


        foods.append({
            "name": food.Long_Desc,
            "id": association.id,
            "quantity": association.quantity,
            "nutrients": nutrient_dict,
            "unit": unit.Msre_Desc,
        })

    return foods  

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

def get_nutrient_unit(nutrient_definitions, nutrient_number):
    nutrient_definition = filter(
       lambda nutrient_definition: 
           nutrient_definition.Nutr_No == str(nutrient_number), 
       nutrient_definitions)[0]
    nutrient_unit = nutrient_definition.Units
    if nutrient_unit == u"µg":
        nutrient_unit = u"mcg"
    unit_precision = nutrient_definition.Num_Dec
   
                
    return nutrient_unit, unit_precision

def format_unit_for_display(value, nutrient_unit, unit_precision):
    if isinstance(value, float):
       value = round(value, int(unit_precision))
    else:
       value = ""
       nutrient_unit = ""
    return value, nutrient_unit
   



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
@app.route('/food_log/saved_meal', methods=['POST'])
@login_required
def saved_meal_post():
    #don't use the reequest.args.get('user') to avoid malicious user.
    user = current_user
    #request.args.get('meal_name') gets the value associated 
    #with the query string 'meal_name' 
    #ex: /add_saved_meal_post?meal_name=breakfast
    selected_foods = request.args.get('selected_foods')
    meal_name = request.args.get('meal_name')


    #think about keys and values. look at the flask documentation for requesting
    #keys and values.



   #do not use 'if not selected_foods' because the id of 0 evaluates to False.
    if selected_foods == None or selected_foods == "":  
        return ""
        #need to first strip leading and trailing commas to create a clean and valid list
        #of strings separated by commas.
    selected_foods = selected_foods.strip(",").split(',')
    
    #create an instance of the Meal model
    #creating a Meal object by calling the Meal constructor.
    #can set any column values as identified in the models, in this case models/meal.py
    #creating a name for the saved_meal 
    saved_meal = Meal(name=meal_name)

    
    #loop through the food_ids to save the selected foods as a meal.
    #selected_foods is a list.
    for food_id in selected_foods:
        #making an instance of the  Class MealFoodAssociation
        meal_food_association = MealFoodAssociation()

        #query the FoodLogFoodAssociation table to get the row (the matching association) that has the specific 
        #food_id.
        food_log_food_association = session.query(FoodLogFoodAssociation).get(int(food_id))

        #access the attribute of the variable which is an instance of the class
        #copy the attributes from the food_log_food_association to the
        #attribute mealfoodassociation
        #integer primary keys are automatically filled in.
        meal_food_association.food_NDB_No = food_log_food_association.food_NDB_No
        meal_food_association.unit_Seq = food_log_food_association.unit_Seq
        meal_food_association.quantity = food_log_food_association.quantity
        #add the saved food to the Meal
        saved_meal.foods.append(meal_food_association)
    #append the saved _meal to the list user.meals
    #save it once. Take it out of the for loop.
    user.meals.append(saved_meal)
        #save the meal
    session.add(saved_meal)
    session.commit()
    #returning an empty string is saying that the code works.
    return ""
    
@app.route('/food_log/add_saved_meal', methods=['POST'])
@login_required
def add_saved_meal_post():
    #don't use the reequest.args.get('user') to avoid malicious user.
    #user_id incorporates the user_id via flask.
    user = current_user
    meal_name = request.args.get('meal_name')
    #query the data base Meal.
    meal = session.query(Meal).filter_by(name=meal_name, user_id=user.id).first()   
    food_log = get_food_log(user)
    for food in meal.foods:
        #food is the name of the food in the MealFoodAssociation
        #create a new FoodLogFoodAssociation() for each MealFoodAssociation
        flfa = FoodLogFoodAssociation()
        #copy over the attributes of the MealFoodAssociation to FoodLogFoodAssociation
        flfa.food_NDB_No = food.food_NDB_No
        flfa.unit_Seq = food.unit_Seq
        flfa.quantity = food.quantity
        #append FoodLogFoodAssociation to food_log.foods
        food_log.foods.append(flfa)
        #send back this info to the client side via html which will then 
        #be sent to the javascript which will insert the info on the page.
    session.commit()
    nutrient_definitions = session.query(NutrientDefinition).all()
    foods = build_food_list(meal.foods, nutrient_definitions)
    return render_template('partial_food_log.html', foods=foods)
    




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
    


    # Get the current food log
    food_log = get_food_log(user)
    foods = build_food_list(food_log.foods, nutrient_definitions)

    with open("dump.json", "w") as f:
        json.dump(foods, f)
    
    # Total the number of nutrients consumed
    totals = defaultdict(lambda: ordered_defaultdict.OrderedDefaultdict(list))
    for food in foods:
        nutrients = food["nutrients"]
        for category_name, category in nutrients.iteritems():
            for nutrient_name, nutrient_tuple in category.iteritems():
                nutrient_value = nutrient_tuple[0]
                subnutrients = nutrient_tuple[1]
                nutrient_unit = nutrient_tuple[2]
                if totals[category_name][nutrient_name] == []:
                    totals[category_name][nutrient_name].append(0)
                    totals[category_name][nutrient_name].append(ordered_defaultdict.OrderedDefaultdict(list))
                    totals[category_name][nutrient_name].append("")
                if not nutrient_value or nutrient_value == "N/A":
                    continue

                totals[category_name][nutrient_name][0] += float(nutrient_value)
                for subnutrient_name, subnutrient_tuple in subnutrients.iteritems():
                    subnutrient_value = subnutrient_tuple[0]
                    subnutrient_unit = subnutrient_tuple[1]
                    if totals[category_name][nutrient_name][1][subnutrient_name] == []:
                        totals[category_name][nutrient_name][1][subnutrient_name].append(0)
                        totals[category_name][nutrient_name][1][subnutrient_name].append("")
                    if not subnutrient_value or subnutrient_value == "N/A":
                        continue
                    totals[category_name][nutrient_name][1][subnutrient_name][0] += subnutrient_value



    foods.append({
        "name": "Totals",
        "nutrients": totals,
    })
    calorie_percentage = (
        totals["Calorie Information"]["Energy_KCAL"][0] *100
        )

    calorie_percentage /= user.get_adjusted_daily_caloric_needs()

    protein_percentage = (
        totals["Protein & Amino Acids"]["Protein"][0] * 100
        )
    protein_percentage /= user.get_adjusted_daily_caloric_needs()

    carbohydrate_percentage = (
        totals["Carbohydrates"]["Carbohydrate, by difference"][0] * 100
        )
    carbohydrate_percentage /= user.get_adjusted_daily_caloric_needs()
    fat_percentage = (
        totals["Fats & Fatty Acids"]["Total lipid (fat)"][0] * 100
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

    try:
        association = FoodLogFoodAssociation(
            food_NDB_No=unit["NDB_No"],
            unit_Seq=unit["Seq"],
            quantity=float(quantity)
        )
    except ValueError as e:
        flash('Please use proper syntax when entering the number or use a decimal point')
        return redirect(url_for('food_log_get'))





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

    # user.selected_food_groups is linked to the nutrition database.
    session.query(UserFoodGroupAssociation).delete()
    for code in food_groups:
        association = UserFoodGroupAssociation(
            food_group_code=code
        )
        user.selected_food_groups.append(association)

    session.commit()
    return ""






