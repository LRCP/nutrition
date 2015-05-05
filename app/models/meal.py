from app import BaseNutrition
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, ForeignKey,Text

class Meal(BaseNutrition):
    #list of atrributes
    __tablename__ = 'meals'
    id = Column(Integer, Sequence('meal_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    foods = relationship('MealFoodAssociation')
    name = Column(Text)


