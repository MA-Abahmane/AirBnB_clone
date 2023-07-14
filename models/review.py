#!/usr/bin/python3
"""
    This module contains a class that inherits BaseModel
    and defines Review of a location
"""

from models.base_model import *


class Review(BaseModel):
    """ inside class Review  """

    place_id = ''
    user_id = ''
    text = ''
