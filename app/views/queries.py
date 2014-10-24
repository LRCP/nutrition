from app import app, session
from app.models.usda import FoodDescription, Weight
from sqlalchemy import or_
from flask import request
import json


@app.route('/queries/<query_string>.json', methods=['GET'])
def query(query_string):

    
    # construct a list of all the groups that we want to use as filters.
    # groups is a list of numbers
    groups = request.args.getlist("group")

    group_filters = [FoodDescription.FdGrp_Cd == group for group in groups]
    foods = session.query(FoodDescription)
    foods = foods.filter(FoodDescription.Long_Desc.ilike('%{}%'.format(query_string)))
    foods = foods.filter(or_(*group_filters))
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
