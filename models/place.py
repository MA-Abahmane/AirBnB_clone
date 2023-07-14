#!/usr/bin/python3
"""
    This module contains a class that inherits BaseModel
    and defines a locations info
"""

from models.base_model import *


class Place(BaseModel):
    """ inside class Place """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
