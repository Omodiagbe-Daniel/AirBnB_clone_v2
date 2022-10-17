#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
from models.state import State
from models.city import City


s = "HBNB_TYPE_STORAGE"
if getenv(s) == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
