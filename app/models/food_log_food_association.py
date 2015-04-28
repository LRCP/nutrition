from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy import Sequence, ForeignKey
from app import BaseNutrition

class FoodLogFoodAssociation(BaseNutrition):
    __tablename__ = 'food_log_food_association'
    id = Column(Integer, Sequence('food_log_food_association_id_seq'), primary_key=True)
    food_log_id = Column(Integer, ForeignKey('food_logs.id'))
    food_NDB_No = Column(Text)
    unit_Seq = Column(Text)
    quantity = Column(Float)

   

