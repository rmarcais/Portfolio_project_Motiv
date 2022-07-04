#!/usr/bin/python3
""" City Module for portfolio project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, that contains department ID, users, events and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    department_id = Column(String(60), ForeignKey('departments.id'),
                           nullable=False)
    users = relationship("User", backref="cities")
    events = relationship("Event", backref="cities")
