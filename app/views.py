
# The views are the handlers that respond to requests from web browsers.
from flask import render_template, flash, request, redirect, url_for, request
from flask.ext.login import login_user, logout_user
from flask.ext.login import current_user, login_required
from app import app, lm, oid, session, ordered_defaultdict
from app.forms import ProfileForm, RegistrationForm, LoginForm
from app.models.association import *
from app.models.foodlog import *
from app.models.user import *
from app.models.usda import *
import json
from sqlalchemy import or_
from app.constants import food_nutrient_dictionary, food_groups_dictionary
from collections import OrderedDict, defaultdict
import sys

@app.route('/')
@app.route('/index')
# def index():
#      user = { 'nickname': 'Linda' } # fake user
#      return render_template("index.html",
#          title = 'Home',
#          user = user)


#next assignment: use food_log as an example.
@app.route('/profile', methods=['GET'])
def profile_get():
    form = ProfileForm(request.form)
    return render_template('profile.html',
        #title is the name of the page for Profile: Nutrition
        title='Profile',
        #make a variable in the template called form. 
        #The value of the form should be
        #equal to the variable form in the local function.
        form=form)


@app.route('/profile', methods=['POST'])
def profile_post():
    form = ProfileForm(request.form)
    #print request.form

    if form.validate():

        #get the user from the database session
        user = session.query(User).filter_by(email="happy").first()
        # do not store the results of calculations using variable defined in
        # models.py That is what models.py is for.
        user.calorie_goal = form.calorie_goal.data
        user.protein_goal = form.protein_goal.data

        user.carbohydrate_goal = form.carbohydrate_goal.data
        user.fat_goal = form.fat_goal.data
        #user.nutrient_goal = form.nutrient_goal.data
        user.birthday = form.birthday.data
        user.set_weight(form.weight.data, form.weight_unit.data)
        user.set_weight_goal(form.weight_goal.data, form.weight_unit.data)
        user.set_height(form.height.data, form.height_unit.data)
        user.gender = form.gender.data    
        user.activity_level = form.activity_level.data
        user.set_weekly_weight_change(form.weekly_change_level.data)
        session.commit()
        #Here we need to save the information enterred by the User.
        #need access to the user object.
        #return redirect(url_for('profile_get'))
        return render_template(
            'profile.html', title='Profile',
            form=form)



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
        total  = total + nutrient_dictionary[key]
    return total

@app.route('/food_log', methods=['GET'])
def food_log_get():
   
    user = session.query(User).filter_by(email="happy").first()
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
                        float(nutrient_value) * association.quantity * float(association.unit.Gm_Wgt)/100
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
def food_log_post():
    user = session.query(User).filter_by(email="happy").first()
    
    quantity = request.form.get('quantity')
    unit = request.form.get('unit')
    #redifine unit to the JSON version to decode JSON
    #print unit
    unit = json.loads(unit)
    food_log = get_food_log(user)
    food = session.query(FoodDescription)
    food = food.filter(FoodDescription.NDB_No==unit["NDB_No"]).first()
    association = Association()
    #quantity is an attribute of a class
    association.quantity = float(quantity)
    #the association will contain one food and one food_log
    association.food = food
    weight = session.query(Weight)
    weight = weight.filter(Weight.NDB_No==association.food.NDB_No, 
        Weight.Seq==unit["Seq"]).first()
    print >>sys.stderr,association.food.NDB_No
    association.unit = weight
    food_log.foods.append(association)
    session.commit()
    #after adding the requests, want to take a look at the food log
    return redirect(url_for('food_log_get'))

@app.route('/food_log/delete/<id>', methods=['GET','POST'])
def delete_food(id):
    association = session.query(Association).filter_by(id=id).first()
    session.delete(association)
    return redirect(url_for('food_log_get'))

    
@app.route('/login', methods=['GET', 'POST'])

@oid.loginhandler
def login():
    
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = session.query(User).filter_by(email="happy").first()
        #login = session.query(LoginForm).filter_by(user=user).first()
        user = User(form.openid.data, form.remember_me.data)
        session.add(user)
    
        return redirect(url_for('index'))
    return render_template(
        'login.html', title='Sign In',
    form=form,
        providers=app.config['OPENID_PROVIDERS'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = session.query(User).filter_by(email="happy").first()
        #register = session.query(RegistrationForm).filter_by(user=user).first()
        user = User(form.username.data, form.email.data, 
            form.password.data)
        session.add(user)
        session.commit()
        return redirect(url_for('login'))
    return render_template(
        'register.html', title="Register",
        form=form)


@lm.user_loader
def load_user(id):  
    return User.query.get(int(id))()

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
    
