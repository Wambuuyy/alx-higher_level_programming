#!/usr/bin/python3
"""
Contains the class definition of a State with a relationship with City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    """
    Class representing a State with a relationship with City.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
