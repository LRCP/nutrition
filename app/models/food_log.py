from app import BaseNutrition
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, ForeignKey, Date
import datetime

class FoodLog(BaseNutrition):
    __tablename__ = 'food_logs'
    id = Column(Integer, Sequence('food_logs_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    foods = relationship('FoodLogFoodAssociation')
    date = Column(Date, default = datetime.datetime.now)
