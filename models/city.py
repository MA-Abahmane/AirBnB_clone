#!/usr/bin/python3
"""
    This module contains a class that inherits BaseModel
    and defines a User city
"""

from models.base_model import *


class City(BaseModel):
    """ inside class City """

    state_id = ''
    name = ''
