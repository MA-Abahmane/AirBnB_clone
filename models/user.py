#!/usr/bin/python3
""" 
    This module contains the class 'User' that inherits from BaseModel
"""

from models.base_model import *


class User(BaseModel):
    """ class User """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
