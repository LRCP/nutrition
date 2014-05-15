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
app.config.from_object('config')
engineUSDA = create_engine('sqlite:///nutrient.db')
engineNutrition = create_engine('sqlite:///app.db')
BaseUSDA = declarative_base()
BaseNutrition = declarative_base()
metadata = MetaData(bind=engineUSDA)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


# Then import needed files already existing in the root folder

from app.models import *
Session = sessionmaker()
session = Session(binds={
    Association:engineNutrition, 
    User:engineNutrition, 
    DataDerivationCodeDescription:engineUSDA, 
    FoodLog:engineNutrition, 
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
    Weight:engineUSDA
    })

# to import the user into our views and access the user, we must first
# define the user. We need the user model to make the user so this must come
# after importing models.
# models.User is used because User is in models.

user = session.query(models.User).filter_by(email='happy').first()
if user is None:
    user = models.User('Linda', 'lp', 'happy')
    session.add(user)
    session.commit()

#food = session.query(models.Food).filter_by(name='kale').first()
#if food is None:
    #food = models.Food('kale', 1, 2, 3, 4)
    #session.add(food)
    #session.commit()

#food = session.query(models.Food).filter_by(name='grapes').first()
#if food is None:
    #food = models.Food('grapes', 1, 2, 3, 4)
    #session.add(food)
   # session.commit()

session.close()

from app import views


