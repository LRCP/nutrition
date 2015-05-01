#first import what is needed to support the code
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

from flask import Flask

# Then initialize the variables
app = Flask(__name__)
# to iterate ove an ordered dictionary in jinja2, import the module enumerate.
# see stackoverflow: http://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2
app.jinja_env.globals.update(enumerate=enumerate)
app.config.from_object('config')
#sqlite lives in the computer
engineUSDA = create_engine('sqlite:///sr27.db')
engineNutrition = create_engine('sqlite:///app.db')
BaseUSDA = declarative_base()
BaseNutrition = declarative_base()
metadata = MetaData(bind=engineUSDA)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



# Then import needed files already existing in the root folder
#can import values, functions, classes.
#need to import al the classes created in app/models
from app.models.user import User
from app.models.food_log import FoodLog
from app.models.food_log_food_association import FoodLogFoodAssociation
from app.models.user_food_group_association import UserFoodGroupAssociation
from app.models.favorite_association import FavoriteAssociation
from app.models.meal import Meal
from app.models.meal_food_association import MealFoodAssociation


from app.models.usda import *

BaseNutrition.metadata.create_all(engineNutrition)

Session = sessionmaker()
session = Session(binds={
    User:engineNutrition,
    FoodLog: engineNutrition,
    FoodLogFoodAssociation:engineNutrition,
    UserFoodGroupAssociation:engineNutrition,
    FavoriteAssociation:engineNutrition,
    DataDerivationCodeDescription:engineUSDA,
    FoodLog:engineNutrition,
    Meal:engineNutrition,
    MealFoodAssociation:engineNutrition,
    FoodDescription:engineUSDA,
    FoodGroupDescription:engineUSDA,

    Footnote:engineUSDA,
    LangualFactorsDescription:engineUSDA,
    LangualFactor:engineUSDA,
    NutrientData:engineUSDA,
    NutrientDefinition:engineUSDA,
    SourcesofData:engineUSDA,
    SourcesOfDataLink:engineUSDA,
    SourceCode:engineUSDA,
    Weight:engineUSDA,

})

# to import the user into our views and access the user, we must first
# define the user. We need the User class to make the user so this must come
# after importing app.models.user.
# User is used because User is in app.models.user.

#need to change the user.
# user = session.query(User).filter_by(email='happy').first()
# if user is None:
#     user = User('Linda', 'lp', 'happy')
#     session.add(user)
#     session.commit()

#session.close()

from app.views import food_log
from app.views import index
from app.views import login
from app.views import logout
from app.views import profile
from app.views import queries
from app.views import register
from app import filters


