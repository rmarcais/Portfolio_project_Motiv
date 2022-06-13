#!/usr/bin/python3
"""sport.py
This module defines the class Sport.
"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Sport(BaseModel, Base):
    """This class defines the sport"""
    __tablename__ = "sports"
    name = Column(String(128), nullable=False)
