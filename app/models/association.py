from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy import Sequence, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from app import BaseNutrition, engineNutrition
from app.models.usda import Weight, FoodDescription

class Association(BaseNutrition):
    __tablename__ = 'association'
    #unique id
    id = Column(Integer, Sequence('association_id_seq'), primary_key=True)
    #relationship between the instance of the Association class and the food_log
    food_logs_id = Column(Integer, ForeignKey('food_logs.id'))
   
    #food_ndb_no = Column(Text, ForeignKey(FoodDescription.NDB_No))
    #this is a column for the first primary key
    unit_ndb_no = Column(Text)
    #create a column for the second primary key
    unit_seq = Column(Text)

    #making a relationship between the association and the weight.
    #when we set the unit variable of an instance of an association,
    #then the unit_ndb_no and the unit_seq columns will be automatically given 
    #the correct value.
    unit = relationship(Weight)
    #food = relationship(FoodDescription)


    #create composite foreign key constraint
    #unit_ndb_no maps to the Weight.NDB_No. unit_sqe maps to Weight.Seq
    __table_args__ = (ForeignKeyConstraint([unit_ndb_no, unit_seq], 
                                           [Weight.NDB_No, Weight.Seq]), {})
                    


    quantity = Column(Float)
    #unit = Column(String)

Association.food = relationship(FoodDescription, backref='foodlog_assocs')
Association.food_description_NDB_No = Column(
    Text, ForeignKey(FoodDescription.__table__.c.NDB_No)
    )
#This is where we create the database.
BaseNutrition.metadata.create_all(engineNutrition)
