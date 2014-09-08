from app import BaseNutrition
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, ForeignKey

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


    

    #foods, an attribute, is being modified to be defined 
    #via the Association Object.
    foods = relationship('Association')