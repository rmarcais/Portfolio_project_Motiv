#!/usr/bin/python3
"""review.py
This module defines the class Review.
"""

from email.policy import default
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """This class defines the review"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
