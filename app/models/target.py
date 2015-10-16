from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy import Sequence
from app import BaseNutrition

class Target(BaseNutrition):
    __tablename__ = 'target'
    #nullable = Flase for columns where values are required. Some values 
    #may not be available and therefore may require a value.
    id = Column(Integer, Sequence('target_id_seq'), primary_key=True)
    group = Column(Text, nullable=False)
    lower_age = Column(Float, nullable=False)
    upper_age = Column(Float, nullable=False)
    #nutrient_no is being referenced as a text because that is how it is referenced in the USDA database
    nutrient_no = Column(Text, nullable=False)
    value = Column(Float)





