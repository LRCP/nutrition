from sqlalchemy import Column, Text, Integer
from sqlalchemy import Sequence, ForeignKey, UniqueConstraint
from app import BaseNutrition

class FavoriteAssociation(BaseNutrition):
    __tablename__ = 'favorite_association'
    id = Column(Integer, Sequence('favorite_association_id_seq'),
        primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    NDB_No = Column(Text)
    popularity = Column(Integer)
    #need a trailing comma to create a tuple.
    __table_args__ = (UniqueConstraint('user_id', 'NDB_No'),)