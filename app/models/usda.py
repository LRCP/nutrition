from app import BaseUSDA, metadata
from sqlalchemy import Table, Column, Text

class DataDerivationCodeDescription(BaseUSDA):
    __table__ = Table(
        'deriv_cd', metadata, Column('Deriv_Cd', Text, primary_key=True),
        autoload=True)

class FoodGroupDescription(BaseUSDA):
    __table__ = Table(
        'fd_group', metadata, Column('FdGrp_Cd', Text, primary_key=True),
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
        Column('Factor_Code', Text, primary_key=True),
        autoload=True)


class NutrientData(BaseUSDA):
    __table__ = Table(
        'nut_data', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Text, primary_key=True), autoload=True)


class NutrientDefinition(BaseUSDA):
    __table__ = Table(
        'nutr_def', metadata, Column('Nutr_No', Text, primary_key=True),
        autoload=True)

class SourceCode(BaseUSDA):
    __table__ = Table(
        'src_cd', metadata, Column('Src_Cd', Text, primary_key=True),
        autoload=True)

class SourcesofData(BaseUSDA):
    __table__ = Table(
        'data_src', metadata, Column('Data_Src_ID', Text, primary_key=True),
        autoload=True)

class SourcesOfDataLink(BaseUSDA):
    __table__ = Table(
        'datsrcln', metadata,
        Column('NDB_No', Text, primary_key=True),
        Column('Nutr_No', Text, primary_key=True),
        Column('DataSrc_ID', Text, primary_key=True),
        autoload=True)


class Weight(BaseUSDA):
    __table__ = Table(
        'weight', metadata, Column('NDB_No', Text, primary_key=True),
        Column('Seq', Text, primary_key=True), autoload=True)

