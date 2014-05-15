from itertools import chain
from sqlalchemy import create_engine, Column, Text
from sqlalchemy import Integer, String, Float, Table, SmallInteger
from sqlalchemy import Sequence, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.associationproxy  import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from app import BaseNutrition, BaseUSDA, engineNutrition, metadata, engineUSDA
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound




#consider renaming association_table to something more description and as plurals
class Association(BaseNutrition):
    __tablename__ = 'association'
    id = Column(Integer, Sequence('association_id_seq'), primary_key=True)
    food_logs_id = Column(Integer, ForeignKey('food_logs.id'))
    #food_des_NDB_No = Column(Text, ForeignKey('food_des.NDB_No'), primary_key=True)
    quantity = Column(Float)
    #extra_data = Column(String(50))
    
    #foodlogs = relationship('FoodLog', backref='foodlog_assocs')

# This code is replaced by the class definition above.
#association_table = Table('association', BaseNutrition.metadata,
    #Column('foods_id', Integer, ForeignKey('foods.id')),
    #Column('food_logs_id', Integer, ForeignKey('food_logs.id')),
    #)

ROLE_USER = 0
ROLE_ADMIN = 1

class User(BaseNutrition):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(64), index = True, unique = True)
    password = Column(String(12))
    email = Column(String(102), index = True, unique = True)
    role = Column(SmallInteger, default = ROLE_USER)
    calorie_goal = Column(Integer)
    protein_goal = Column(Integer)
    carbohydrate_goal = Column(Integer)
    fat_goal = Column(Integer)
    weight = Column(Integer)
    
    #one to many
    food_logs = relationship('FoodLog', backref='user', lazy = 'dynamic')

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
        return "<User('%s','%s', '%s')>" % (self.name, self.password, self.email)

#class FoodDescription(BaseUSDA):
    #__table__ = Table(
        #'food_des', metadata, Column('NDB_No', Text, primary_key=True),
        #autoload=True)
    #foodlogs = relationship("FoodLog", backref="food_des_assocs")

#should class Food be deleted?
#class Food(BaseNutrition):#lists the nutrients.
    #__tablename__ = 'foods'
    #id = Column(Integer, Sequence('foods_id_seq'), primary_key=True)
    #name = Column(String(50))
   # calorie = Column(Integer)
    #protein = Column(Integer)
    #carbohydrate = Column(Integer)
    #fat = Column(Integer)
    #food_log_id = Column(Integer, ForeignKey('food_log.id'))
    #backref is a name to refer back to the original connection.

    
    
    #def __init__(self, name, calorie, protein, carbohydrate, fat):
        #self.name = name
        #self.calorie = calorie
       # self.protein = protein
        #self.carbohydrate = carbohydrate
        #self.fat = fat

    #def __repr__(self):
        #return "<Food('%s','%d', '%d', '%d', '%d')>" % (self.name, 
            #self.calorie, self.protein, self.carbohydrate, self.fat)

class FoodLog(BaseNutrition):#continue using users as a model
# FoodLog is a list of foods eaten and the quantity eaten.
# be sure to read building a realtionship in the tutorial. Need to consider ForeignKey
# many to one is for the relationship between FoodLog and User
# a user can have multiple food_logs but food_log can have one user
# many to many is for relationship between FoodLog and Food
    __tablename__ = 'food_logs'
    id = Column(Integer, Sequence('food_logs_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))#many food_logs to one user
    #timestamp = Column(DateTime)

    #foods is being modified to be defined via the Association Object.
    #foods = relationship('Food', secondary=association_table, backref='food_logs')#many to many relationship
    #food_log may have many foods
    foods = relationship('Association')
        
    #instantiation not needed when used with SQLAlchemy.
    #AQLAlchemy automatically gives the __init__ constructor.
    #def __init__(self, name, quantity):
        #self.food_name = name
        #self.quantity = quantity
        
    #def __repr__(self):
        #return "<FoodLog('%s','%d')>" % (self.food_name, self.quantity)

# only create meta data in databases we are creating, 
# not in preexisting databases.

#FoodLog.food_description_NDB_No = Column(Text, ForeignKey(FoodDescription.__table__.c.NDB_No))




class DataDerivationCodeDescription(BaseUSDA):
    __table__ = Table(
        'deriv_cd', metadata, Column('Deriv_Cd', Integer, primary_key=True), 
        autoload=True)

class FoodGroupDescription(BaseUSDA):
    __table__ = Table(
        'fd_group', metadata, Column('FdGrp_Cd', Integer, primary_key=True), 
        autoload=True)

class FoodDescription(BaseUSDA):
    __table__ = Table(
        'food_des', metadata, Column('NDB_No', Text, primary_key=True),
        autoload=True)

class Footnote(BaseUSDA):
    __table__ = Table(
        'footnote', metadata, Column('NDB_No', Text, primary_key=True), 
        autoload=True)

class LangualFactorsDescription(BaseUSDA):
    __table__ = Table(
        'langdesc', metadata, Column('Factor_Code', Text, primary_key=True), 
        autoload=True)

class LangualFactor(BaseUSDA):
    __table__ = Table(
        'langual', metadata, Column('NDB_No', Text, primary_key=True), 
        Column('Factor_Code', Integer, primary_key=True),
        autoload=True)


class NutrientData(BaseUSDA):
    __table__ = Table(
        'nut_data', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Integer, primary_key=True), autoload=True)


class NutrientDefinition(BaseUSDA):
    __table__ = Table(
        'nutr_def', metadata, Column('Nutr_No', Integer, primary_key=True), 
        autoload=True)

class SourceCode(BaseUSDA):
    __table__ = Table(
        'src_cd', metadata, Column('Src_Cd', Integer, primary_key=True), 
        autoload=True)

class SourcesofData(BaseUSDA):
    __table__ = Table(
        'data_src', metadata, Column('Data_Src_ID', Integer, primary_key=True), 
         autoload=True)

class SourcesOfDataLink(BaseUSDA):
    __table__ = Table(
        'datsrcln', metadata, 
        Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Integer, primary_key=True), 
        Column('DataSrc_ID', Integer, primary_key=True), 
        autoload=True)


class Weight(BaseUSDA):
    __table__ = Table(
        'weight', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Seq', Integer, primary_key=True), autoload=True)


Association.food = relationship(FoodDescription, backref='foodlog_assocs')
Association.food_description_NDB_No = Column(Text, ForeignKey(FoodDescription.__table__.c.NDB_No))
BaseNutrition.metadata.create_all(engineNutrition)





