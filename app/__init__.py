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

session.close()

from app import views


