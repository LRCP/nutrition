from app import BaseNutrition
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence, SmallInteger, Float, Text, Date
from sqlalchemy.orm import relationship
from datetime import date

ROLE_USER = 0
ROLE_ADMIN = 1

class User(BaseNutrition):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(64), index=True, unique=True)
    password = Column(String(12))
    email = Column(String(102), index=True, unique=True)
    role = Column(SmallInteger, default=ROLE_USER)
    protein_goal = Column(Integer)
    carbohydrate_goal = Column(Integer)
    fat_goal = Column(Integer)
    weight_in_kilograms = Column(Integer)
    weight_goal = Column(Integer)
    height_in_meters = Column(Float)
    gender = Column(String)
    weekly_weight_change = Column(Integer)
    openid = Column(String(64),
            Sequence('user_openid_seq'), index=True, unique=True)
    remember_me = Column(String, default=False)
    username = Column(String(25))
    confirm = Column(Text)
    calorie_goal = Column(Integer)
    birthday = Column(Date)
    #nutrient_goal = Column(Float)
    activity_level = Column(String)
    caloric_change_weekly = Column(Integer)
    caloric_change_daily = Column(Integer)
    adjusted_daily_caloric_needs = Column(Integer)
    body_mass_index = Column(Float)
    
    def get_body_mass_index(self):
        bmi = self.weight_in_kilograms / (self.height_in_meters **2)
        return bmi

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
           #self refers to the user's object, the instance of the class,  
           #whoever is logged in.
        return self


    #def set_height(self, number_a, number_b=0, unit='height_in_meters'):
    def set_height(self, number_a, unit='height_in_meters'):
        if unit == 'height_in_meters':
            self.height_in_meters = number_a
        # elif unit == 'height_in_feet':
        #     self.height_in_meters = number_a * .30 + number_b *.03
        elif unit == 'height_in_inches':
            self.height_in_meters = number_a /39.37
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
        dietary_thermogenesis_calories = (
            .10 * (self.get_basal_metabolic_rate() +
                self.get_activity_calories())
            )
        return dietary_thermogenesis_calories

    def get_caloric_needs_daily(self):
        caloric_needs_daily = (
            self.get_basal_metabolic_rate() +
            self.get_activity_calories() +
            self.get_dietary_thermogenesis_calories()
            )
        return caloric_needs_daily
    
    
    def get_adjusted_daily_caloric_needs(self):
        adjusted_daily_caloric_needs = (
            self.get_caloric_needs_daily() + self.weekly_weight_change / 700
            )
        return adjusted_daily_caloric_needs

   
    #one to many
    food_logs = relationship('FoodLog', backref='user', lazy='dynamic')

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
        return "<User('%s','%s', '%s')>" % (self.name,
            self.password, self.email)


