from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy import Sequence, ForeignKey
from app import BaseNutrition

class MealFoodAssociation(BaseNutrition):
    __tablename__ = 'meal_food_association'
    id = Column(Integer, Sequence('meal_food_association_id_seq'), primary_key=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    food_NDB_No = Column(Text)
    unit_Seq = Column(Text)
    quantity = Column(Float)