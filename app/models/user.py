from app import BaseNutrition
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence, SmallInteger, Float, Text, Date
from sqlalchemy.orm import relationship
from datetime import date
from werkzeug.security import generate_password_hash

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
    remember_me = Column(String, default=False)
    username = Column(String(25))
    confirm = Column(Text)
    calorie_goal = Column(Integer)
    birthday = Column(Date)
    activity_level = Column(String)
    caloric_change_weekly = Column(Integer)
    caloric_change_daily = Column(Integer)
    adjusted_daily_caloric_needs = Column(Integer)
    body_mass_index = Column(Float)
    selected_food_groups = relationship('UserFoodGroupAssociation')

    def get_body_mass_index(self):
        bmi = self.weight_in_kilograms / (self.height_in_meters **2)
        return bmi

    def get_age(self):
        age = date.today() - self.birthday
        return age.days / 365

    def set_weekly_weight_change(self, weekly_change_level):
        weekly_weight_change_dictionary = {
            'minus_two_pounds': -2,
            'minus_one_and_one_half_pound': -1.5,
            'minus_one_pound': -1,
            'minus_one_half_pound': -.5,
            'maintain': 0,
            'plus_one_half_pound': .5,
            'plus_one_pound': 1,
            'plus one_and_one_half_pound': 1.5,
            'plus_two_pounds': 2
        }
        if weekly_change_level in weekly_weight_change_dictionary:
            self.weekly_weight_change = (
                weekly_weight_change_dictionary[weekly_change_level]
                )
        else:
            raise ValueError("The weekly change level " + weekly_change_level + " is incorrect.")
        return self

    def get_weekly_change_level(self):
        weekly_change_level_dictionary = {
            -2: 'minus_two_pounds',
            -1.5: 'minus_one_and_one_half_pound',
            -1: 'minus_one_pound',
            -.5: 'minus_one_half_pound',
            0: 'maintain',
            .5: 'plus_one_half_pound',
            1:'plus_one_pound',
            1.5: 'plus one_and_one_half_pound',
            2: 'plus_two_pounds'
        }

        if self.weekly_weight_change in weekly_change_level_dictionary:
            return weekly_change_level_dictionary[self.weekly_weight_change]

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


    def set_height(self, number_a):
        self.height_in_meters = number_a
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

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.username, self.name,
                                            self.email)

