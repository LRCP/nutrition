from sqlalchemy import Column, Text, Integer
from sqlalchemy import Sequence, ForeignKey
from app import BaseNutrition

class UserFoodGroupAssociation(BaseNutrition):
    __tablename__ = 'user_food_group_association'
    id = Column(Integer, Sequence('user_food_group_association_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    food_group_code = Column(Text)

