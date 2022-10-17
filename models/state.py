#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
