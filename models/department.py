#!/usr/bin/python3
""" City Module for portfolio project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Department(BaseModel, Base):
    """ The department class, contains a name and cities"""
    __tablename__ = "departments"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="department")
