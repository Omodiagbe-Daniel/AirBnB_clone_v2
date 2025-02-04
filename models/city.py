#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
