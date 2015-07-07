from app import app, session
from app.models.usda import FoodDescription, Weight
from app.models.meal import Meal
from sqlalchemy import or_
from flask import request
import json

#we are returning json data
#can type into the url bar: localhost:5000/saved
@app.route('/queries/<query_string>.json', methods=['GET'])
#create a function with thestring passed in. Lines 8 and 10 must match up.
def query_foods(query_string):

    
    # construct a list of all the groups that we want to use as filters.
    # groups is a list of numbers
    groups = request.args.getlist("group")

    group_filters = [FoodDescription.FdGrp_Cd == group for group in groups]
    foods = session.query(FoodDescription)
    foods = foods.filter(FoodDescription.Long_Desc.ilike('%{}%'.format(query_string)))
    foods = foods.filter(or_(*group_filters))
    # .all(0)sends the query to the database and try to get back a list of items.)
    foods = foods.all()
    food_list = []
    for food in foods:
        #find all the weights that match the foods.
        unit_query = session.query(Weight).filter(Weight.NDB_No == \
        food.NDB_No).all()
        unit_list = []
        for unit in unit_query:
            unit_list.append({
                "name": unit.Msre_Desc,
                "Gm_Wgt": unit.Gm_Wgt,
                "NDB_No": unit.NDB_No,
                "Seq": unit.Seq,
                })
        food_list.append({
            "name": food.Long_Desc,
            "units": unit_list
            })
        #to reference units this is the code:
        #food_list[0]
        #food_list[0]["units"]
        #to test queries: type localhost:5000/queries/butter, salted.json
    return json.dumps(food_list)

#can type into the url bar: localhost:5000/saved_meals/<query_string>.json
#ex: localhost:5000/saved_meals/butter.json
#use <path:query_string> to allow slashes in the query string variable.
#see http://flask.pocoo.org/snippets/76/
@app.route('/saved_meals/<path:query_string>.json', methods=['GET'])
#or app.route("saved_meals.json")
def query_saved_meals(query_string):
    #query database called saved_meals
    #construct a query that has the name matching the query string.
    #assign variable saved_meals to the querying of what is in the Meal class.
    saved_meals = session.query(Meal)
    #ilike is case insensitive
    #find the meals that have been typed in '%{}%' and regurn it as a query_string
    saved_meals = saved_meals.filter(Meal.name.ilike('%{}%'.format(query_string)))
    #convert the object designated as the variable saved_meals into a dictionary 
    #using .all() that
    #python can work with.
    saved_meals = saved_meals.all()
    saved_meals_list = []
    for saved_meal in saved_meals:
        saved_meals_list.append({
            "name": saved_meal.name,
            })



    return json.dumps(saved_meals_list)
