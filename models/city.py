#!/usr/bin/python3
""" City Module for portfolio project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    department_id = Column(String(60), ForeignKey('departments.id'), nullable=False)

