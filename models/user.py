#!/usr/bin/python3
"""user.py
This module defines the class User.
"""


from email.policy import default
from sqlalchemy import Column, String, Table, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from models.event import event_user
from flask_login import UserMixin

user_sport = Table('user_sport', Base.metadata,
                          Column('user_id', String(60),
                                 ForeignKey('users.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('sport_id', String(60),
                                 ForeignKey('sports.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class User(BaseModel, Base, UserMixin):
    """This class defines the user's informations"""
    __tablename__ = "users"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    bio = Column(String(1024), nullable=True, default="No bio")
    sports = relationship("Sport",
                                 secondary=user_sport,
                                 viewonly=False)
    reviews = relationship("Review",
                               backref="user",
                               cascade="all, delete, delete-orphan")
    events = relationship("Event",
                                 secondary=event_user,
                                 viewonly=False)
