#!/usr/bin/python3
"""event.py
This module defines the class Event.
"""

from email.policy import default
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models

event_user = Table('event_user', Base.metadata,
                          Column('event_id', String(60),
                                 ForeignKey('events.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('user_id', String(60),
                                 ForeignKey('users.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

class Event(BaseModel, Base):
    """This class defines an event"""

    __tablename__ = "events"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    sport_id = Column(String(60), ForeignKey("sports.id"), nullable=False)
    description = Column(String(1024), nullable=True)
    title = Column(String(128), nullable=False)
    date = Column(String(64), nullable=False, default="No description")

    number_participants = Column(Integer, nullable=False, default=0)
    users = relationship("User",
                                 secondary=event_user,
                                 viewonly=False)
