from itertools import chain
from sqlalchemy import create_engine, Column, Text
from sqlalchemy import Integer, String, Float, Table, SmallInteger
from sqlalchemy import Sequence, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.associationproxy  import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from app import BaseNutrition, BaseUSDA, engineNutrition, metadata, engineUSDA
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound





class Association(BaseNutrition):
    __tablename__ = 'association'
    id = Column(Integer, Sequence('association_id_seq'), primary_key=True)
    food_logs_id = Column(Integer, ForeignKey('food_logs.id'))
    quantity = Column(Float)
    

ROLE_USER = 0
ROLE_ADMIN = 1

class User(BaseNutrition):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(64), index = True, unique = True)
    password = Column(String(12))
    email = Column(String(102), index = True, unique = True)
    role = Column(SmallInteger, default = ROLE_USER)


    calorie_goal = Column(Integer)
    protein_goal = Column(Integer)
    carbohydrate_goal = Column(Integer)
    fat_goal = Column(Integer)
    weight_unit = Column(String)

    #if weight_unit_selected = 'weight_in-kilograms':
        # weight_in _kilograms = weight
    #if weight_unit_selected = 'weight_in_pounds':
        #weight_in_kilograms = int('weight_in_pounds') * .45
    #if weight_unit_selected = 'weight_in_stones'):
    #   weight_in_kilograms = int('weight_in_stones') * 6.35

    weight_in_kilograms = Column(Integer)
    weight_goal = Column(Integer)
    weight_goal_unit = Column(String)
    height_unit = Column(String)

    #if height_unit = 'Height in Feet':
    #   height_in-meters = int('Height In Feet') *.30 + int('Height in Inches) * .03    
    height_in_meters = Column(Float)
    gender = Column(String)
    activity_level = Column(String)

    #basal_metabolic_rate (BMR)= 
    #male_body_weight in pounds * 11 or
    #male_weight_in_kilograms * 2.2 * 11

    #female_body_weight x 10.1
    #if gender = 'Male':
        #basal_metabolic_rate = weight_in_kilograms * 2.2 * 11
    #if gender = 'Female':
        #basal_metabolic_rate = weigt_in_kilograms * 2.2 * 10.1
    basal_metabolic_rate = Column(Integer)
    
    #activity_calories = basal_metabolic_rate * activity_level_percentage
    #inactive = .30
    #average = .50
    #active = .75    
    activity_calories = Column(Integer)
    
    #dietary_thermogenesis_calories = 10%(BMR + activity_calories)
    dietary_thermogenesis_calories = Column(Integer)
    
    #caloric_needs = (BMR + activity_calories + thermogenesis_calories)
    #+- 10%
    caloric_needs = Column(Integer)
    
    weight_change_goal = Column(Float)
    age = Column(Integer)
    birthdate = Column(Integer)

    #caloric_change_daily = caloric_need + 
    caloric_change_daily = Column(Integer)
    
    
    
    
    
    
    calorie_needs_absolute = Column(Integer)
    calorie_needs_ = Column(Integer)
    
    
    protein_ratio_goal = Column(Integer)
    carbohydrate_ratio_goal = Column(Integer)
    fat_ratio_goal = Column(Integer)
    help = Column(Text)

    #create functions def set_activity_level(level): example:
#def set_activity_level(self, level):
#if level == "inacitive":
#self.activity_level = 0.3
#user.set_activity_level(form.activity_level)
    



    # Consider asking for the following information:
    # User_gender: Male or Female
    # User_weight: Output in both kg and pounds
    # User_height:: Output in cm and feet/inches
    # Caloric Needs is based on: 
    #     Basal Metabolic Rate + Activity Calories + Thermogenesis Calories +- 10%
    #     Basal Metabolic Rate: 
    #         Men: User_weight in pounds x 11
    #         Women: User_weight in pounds x 10.1            
    #     Activity Calories: 
    #         Inactive: Less than 2 hours of moving: Basal Metabolic Rate x 30%
    #         Average: Sitting most of the day, walking or standing 2-4
    #            hours, no strenous activity: Basal Metabolic Rate X 50%
    #         Active(physically active 4 or more hours each day, little   
    #             sitting or standing, some strenuous activity):
    #             Basal Metabolic Rate x 75%
    #     Dietary Thermogenesis Calories: 10%(Basal Metabolic Rate + physical activity calories)
    # Weight Goal:
    #     Maintain Weight: Caloric Needs
    #     Lose Weight: Caloric Needs - [(Pounds_per_week_to_lose) x 3500 calories] = Number of calories per week
    #     Gain Weight: Caloric Needs + [(Pounds_per_week_to_gain) x 3500 calories] = Number of calories per week.
    #     Calories per week may be allocated equally or unequally throughout the week. Calories to lose or gain can be devided between caloric intake and activity.
    # Macronutrient Ratio Targets:
    #     Enter desired ratio of calories from Protein, Carbs and Fats:
    #         Protein:   Carbs:   Fats:

   
    #one to many
    food_logs = relationship('FoodLog', backref='user', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.password, self.email)

class FoodLog(BaseNutrition):
# FoodLog is a list of foods eaten and the quantity eaten.
# many to one is for the relationship between FoodLog and User
# many to many is for relationship between FoodLog and Food
    __tablename__ = 'food_logs'
    id = Column(Integer, Sequence('food_logs_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))#many food_logs to one user
    #timestamp = Column(DateTime)

    #foods is being modified to be defined via the Association Object.
    foods = relationship('Association')
 

class DataDerivationCodeDescription(BaseUSDA):
    __table__ = Table(
        'deriv_cd', metadata, Column('Deriv_Cd', Integer, primary_key=True), 
        autoload=True)

class FoodGroupDescription(BaseUSDA):
    __table__ = Table(
        'fd_group', metadata, Column('FdGrp_Cd', Integer, primary_key=True), 
        autoload=True)

class FoodDescription(BaseUSDA):
    __table__ = Table(
        'food_des', metadata, Column('NDB_No', Text, primary_key=True),
        autoload=True)

class Footnote(BaseUSDA):
    __table__ = Table(
        'footnote', metadata, Column('NDB_No', Text, primary_key=True), 
        autoload=True)

class LangualFactorsDescription(BaseUSDA):
    __table__ = Table(
        'langdesc', metadata, Column('Factor_Code', Text, primary_key=True), 
        autoload=True)

class LangualFactor(BaseUSDA):
    __table__ = Table(
        'langual', metadata, Column('NDB_No', Text, primary_key=True), 
        Column('Factor_Code', Integer, primary_key=True),
        autoload=True)


class NutrientData(BaseUSDA):
    __table__ = Table(
        'nut_data', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Integer, primary_key=True), autoload=True)


class NutrientDefinition(BaseUSDA):
    __table__ = Table(
        'nutr_def', metadata, Column('Nutr_No', Integer, primary_key=True), 
        autoload=True)

class SourceCode(BaseUSDA):
    __table__ = Table(
        'src_cd', metadata, Column('Src_Cd', Integer, primary_key=True), 
        autoload=True)

class SourcesofData(BaseUSDA):
    __table__ = Table(
        'data_src', metadata, Column('Data_Src_ID', Integer, primary_key=True), 
         autoload=True)

class SourcesOfDataLink(BaseUSDA):
    __table__ = Table(
        'datsrcln', metadata, 
        Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Integer, primary_key=True), 
        Column('DataSrc_ID', Integer, primary_key=True), 
        autoload=True)


class Weight(BaseUSDA):
    __table__ = Table(
        'weight', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Seq', Integer, primary_key=True), autoload=True)


Association.food = relationship(FoodDescription, backref='foodlog_assocs')
Association.food_description_NDB_No = Column(Text, ForeignKey(FoodDescription.__table__.c.NDB_No))
#This is where we create the database.
BaseNutrition.metadata.create_all(engineNutrition)





