from itertools import chain
from sqlalchemy import create_engine, Column, Text, Date
from sqlalchemy import Integer, String, Float, Table, SmallInteger
from sqlalchemy import Sequence, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.associationproxy  import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from app import BaseNutrition, BaseUSDA, engineNutrition, metadata, engineUSDA
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from datetime import datetime
from datetime import date, timedelta






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
    protein_goal = Column(Integer)
    carbohydrate_goal = Column(Integer)
    fat_goal = Column(Integer)
    weight_in_kilograms = Column(Integer)
    weight_goal = Column(Integer)
    height_in_meters = Column(Float)
    gender = Column(String)
   
    
    weekly_weight_change = Column(Integer)
    openid = Column(String(64), Sequence('user_openid_seq'), index = True, unique = True)
    remember_me = Column(String, default=False)
    username = Column(String(25))
    confirm = Column(Text)
    calorie_goal = Column(Integer)
    birthday = Column(Date)
    #nutrient_goal = Column(Float)
    activity_level = Column(String)
    caloric_change_weekly = Column(Integer)
    caloric_change_daily = Column(Integer)
    

    def get_age(self):
        age = date.today() - self.birthday
        return age.days / 365
  
    def set_weekly_weight_change(self, weekly_change_level):      
        if weekly_change_level == 'minus_two_pounds':
            self.weekly_weight_change = -2 * .45
        elif weekly_change_level == 'minus_one_and_one_half_pound':
            self.weekly_weight_change = -1.5 * .45
        elif weekly_change_level == 'minus_one_pound':
            self.weekly_weight_change = -1 * .45
        elif weekly_change_level == 'minus_one_half_pound':
            self.weekly_weight_change = -.5 * .45
        elif weekly_change_level == 'maintain':
            self.weekly_weight_change = 0 * .45
        elif weekly_change_level == 'plus_one_half_pound':
            self.weekly_weight_change = .5 * .45
        elif weekly_change_level == 'plus_one_pound':
            self.weekly_weight_change = 1 * .45
        elif weekly_change_level == 'plus one_and_one_half_pound':
            self.weekly_weight_change = 1.5 * .45
        elif weekly_change_level == 'plus_two_pounds':
            self.weekly_weight_change = 2 * .45
        return self

    def get_caloric_change_weekly(self):
        caloric_change_weekly = self.weekly_weight_change * 3500
        return caloric_change_weekly
    def get_caloric_change_daily(self):
        caloric_change_daily = self.get_caloric_change_weekly() / 7
        return caloric_change_daily
    
    #do I need to say unit='weight_in_kilograms'?
    def set_weight_goal(self, number, unit):
        if unit == 'weight_in_kilograms':
            self.weight_goal = number
        elif unit == 'weight_in_pounds':
            self.weight_goal = number * .45
        elif unit == 'weight_in_stones':
            self.weight_goal = number * 6.35
        return self


    #do I need to say unit = 'weight_in_kilograms'? 
    def set_weight(self, number, unit):
        if unit == 'weight_in_kilograms':
           self.weight_in_kilograms = number
        elif unit == 'weight_in_pounds':
            self.weight_in_kilograms = number * .45
        elif unit == 'weight_in_stones':
           self.weight_in_kilograms = number * 6.35
           #self refers to the user's object, the instance of the class,  whoever is logged in.
        return self


    def set_height(self, number_a, number_b=0, unit='height_in_meters'):
        if unit == 'height_in_meters':
            self.height_in_meters = number_a
        elif unit == 'height_in_feet':
            self.height_in_meters = number_a * .30 + number_b *.03
        return self

    #need setter functions for height,activity
    #for simple values, don't need addtional arguments.
    def get_basal_metabolic_rate(self):
        if self.gender == 'male':
            basal_metabolic_rate = self.weight_in_kilograms * 2.2 * 11
        elif self.gender == 'female':
            basal_metabolic_rate = self.weight_in_kilograms * 2.2 * 10.1
        return basal_metabolic_rate

    #write more getters 
    def get_activity_calories(self): 
        if self.activity_level == 'inactive':
            activity_calories = self.get_basal_metabolic_rate() * .30
        elif self.activity_level == 'average':
            activity_calories = self.get_basal_metabolic_rate() * .50
        elif self.activity_level == 'active':
            activity_calories = self.get_basal_metabolic_rate() * .75
        return activity_calories


    def get_dietary_thermogenesis_calories(self):
        dietary_thermogenesis_calories = .10 * (self.get_basal_metabolic_rate() + self.get_activity_calories())
        return dietary_thermogenesis_calories

    def get_caloric_needs_daily(self):
        caloric_needs_daily= (
            self.get_basal_metabolic_rate() + 
            self.get_activity_calories() + 
            self.get_dietary_thermogenesis_calories()
            )
        return caloric_needs_daily
    
    
    def get_adjusted_daily_caloric_needs(self):
        adjusted_daily_caloric_needs = self.get_caloric_needs_daily() + self.weekly_weight_change / 700
        return adjusted_daily_caloric_needs
    
        
    #     Maintain Weight: Caloric Needs
    #     Lose Weight: Caloric Needs - [(Pounds_per_week_to_lose) x 3500 calories] = Number of calories per week
    #     Gain Weight: Caloric Needs + [(Pounds_per_week_to_gain) x 3500 calories] = Number of calories per week.
    #     Calories per week may be allocated equally or unequally throughout the week. Calories to lose or gain can be devided between caloric intake and activity.

    
    
    #caloric_change_daily = caloric_need + 
    #caloric_change_daily = Column(Integer) 
    #calorie_needs_ = Column(Integer)

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
    # protein_consumed = Column(Integer)
    # carbohydrate_consumed = Column(Integer)
    # fat_consumed = Column(Integer)
    # vitamins_consumed = Column(Float)
    # minerals_consumed = Column(Float)
    # other_consumed = Column(Float)
    # total_calories_consumed = Column(Integer)


    #def get_total_calories:
    #   Energy_KCAL = 0
    #   for food in self.foods:
    #       Energy_KCAL += food.Energy_KCAL
    #   return calories

    #def get_protein: 
    #   protein = 0
    #   for food in self.foods:
    #       protein +=food.protein
    #   return protein
    #def get_carbohydrates:
    #def get_fat:
    #def get_other:
    #def get_vitamins:
    #def get_minerals:


    

    #foods, an attribute, is being modified to be defined via the Association Object.
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





