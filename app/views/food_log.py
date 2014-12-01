from app import app, session, ordered_defaultdict
from app.models.foodlog import FoodLog
from flask.ext.login import login_required, current_user
from flask import redirect, url_for, render_template, request
from app.models.usda import *
from app.models.association import *
from app.constants import food_nutrient_dictionary
from collections import OrderedDict, defaultdict
import json
import sys
from sqlalchemy import or_

def get_food_log(user):
    #pass the user as a parameter
    
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
    #gets the food groups list from the database
    #session.query(FoodGroupDescription) is a function that returns a variable.
    if user.protein_goal == None:
        return redirect(url_for('profile_get'))

    food_groups_list = session.query(FoodGroupDescription).order_by(
        FoodGroupDescription.FdGrp_Desc).all()
    #pylint suggested FdGrp_Cd
    #food_groups_list = session.query(FoodGroupDescription).order_by(
    #    FoodGroupDescription.FdGrp_Cd).all()
    food_log = get_food_log(user)
    
    # The food_log contains a list of associations between foods and quantities.
    #creating a list of dictionaries
    food_nutrient_list = []
    for association in food_log.foods:
        nutrients = session.query(NutrientData).filter_by(
            NDB_No=association.food.NDB_No).all()
        weights = session.query(Weight).filter_by(
            NDB_No=association.food.NDB_No).all()
            
        
        
        
        #get the nutrient values associated with the food
        #food_nutrient_dictionary is a dictionary with 
        #   a key called nutrient_category_name, and 
        #   a value called OrderedDictionary 
        #nutrient_category_name is the key in food_nutrient_dictionary which is a string
        #nutrient_category_dic is the value in food_nutrient_dictionary which is an Ordered Dictionary
        #values_nutrient_category is an empty dictionary
        #contains the amount of values of each food
        values_nutrient_dictionary = {}
        #find the OrderedDict() for each nutrient_category_dictionary
        for nutrient_category_name in food_nutrient_dictionary:
            nutrient_category_dictionary = food_nutrient_dictionary[nutrient_category_name]
            values_nutrient_category_dictionary = values_nutrient_dictionary[nutrient_category_name] = OrderedDict()
            for nutrient_name in nutrient_category_dictionary:        
                nutrient_number = nutrient_category_dictionary[nutrient_name]
                try:
                    
                    #remember that the USDA database is populated by strings 
                    #and references tonumbers must be converted into floats.
                    nutrient_value = next(
                        x.Nutr_Val for x in nutrients if int(x.Nutr_No) == nutrient_number)                 
                    values_nutrient_category_dictionary[nutrient_name] = (
                        float(nutrient_value) *
                        association.quantity *
                        float(association.unit.Gm_Wgt)/100
                        )
                except StopIteration:
                    values_nutrient_category_dictionary[nutrient_name] = "N/A"
         
        #example           
        #values_nutrient_dictionary["Carbohydrates"]["Fiber"]
        ffa = values_nutrient_dictionary["Fats & Fatty Acids"]
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
        
        food_nutrient_list.append({
            "name": association.food.Long_Desc,
            "nutrients": values_nutrient_dictionary,
            "quantities": association.quantity,
            "unit": association.unit.Msre_Desc,
            "id": association.id
            })
        #create a new dictionary totalling the amount of nutrients consumed.
        #make the dictionary a nested dictionary to show the category_name
    totals = defaultdict(lambda: ordered_defaultdict.OrderedDefaultdict(float))
    for food_dictionary in food_nutrient_list:
        nutrient_category_dictionary = food_dictionary["nutrients"]
        for nutrient_category_name in nutrient_category_dictionary:
            nutrient_dictionary = nutrient_category_dictionary[nutrient_category_name]
            for nutrient_name in nutrient_dictionary:
                if nutrient_dictionary[nutrient_name] != "N/A":
                    totals[nutrient_category_name][nutrient_name] += nutrient_dictionary[nutrient_name]
    #to debug:
    # for nutrient_category_name in totals:
    #     nutrient_dictionary = totals[nutrient_category_name]
    #     for nutrient_name in nutrient_dictionary:  
    #         print "{}: {}: {}".format(nutrient_category_name, nutrient_name, nutrient_dictionary[nutrient_name])  


    food_nutrient_list.append({
        "name": "Totals",
        "nutrients": totals,
        })

    return render_template(
        'food_log.html', title="FoodLog",
        food_nutrient_list=food_nutrient_list,
        food_groups_list=food_groups_list,
        # pass the user into the template. 
        # need a user object to display something in python on views.
        user=user
        )
    

@app.route('/food_log', methods=['POST'])
@login_required
def food_log_post():
    user = current_user
    
    quantity = request.form.get('quantity')
    unit = request.form.get('unit')
    #redifine unit to the JSON version to decode JSON
    #print unit
    unit = json.loads(unit)
    food_log = get_food_log(user)
    food = session.query(FoodDescription)
    food = food.filter(FoodDescription.NDB_No == unit["NDB_No"]).first()
    association = Association()
    #quantity is an attribute of a class
    association.quantity = float(quantity)
    #the association will contain one food and one food_log
    association.food = food
    weight = session.query(Weight)
    weight = weight.filter(Weight.NDB_No == association.food.NDB_No,
                Weight.Seq == unit["Seq"]).first()
    print >>sys.stderr, association.food.NDB_No
    association.unit = weight
    food_log.foods.append(association)
    session.commit()
    #after adding the requests, want to take a look at the food log
    #http://stackoverflow.com/a/11774434/2561528
    #get the groups and print them out
    #split the list of numbers into an actual list.
    return redirect(url_for('food_log_get'))

@app.route('/food_log/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete_food(id):
    association = session.query(Association).filter_by(id=id).first()
    session.delete(association)
    return redirect(url_for('food_log_get'))

@app.route('/food_log/selected_food_groups', methods=['GET', 'POST'])
@login_required
def selected_food_groups():
    #? is a query string which gets info from front end to back end.
    #queries retrieve one long list of one string.
    #need to split up the string with string.split method.
    #remember the food_group codes are stored as texts, not integers.
    food_groups = request.args.get('food_groups')
    if food_groups == None:
        return ""
    food_groups = food_groups.split(',')
    group_filters = [FoodGroupDescription.FdGrp_Cd == group for group in food_groups]
    food_groups = session.query(FoodGroupDescription)
    food_groups = food_groups.filter(or_(*group_filters))
    food_groups = food_groups.all()


    print food_groups
    return ""




