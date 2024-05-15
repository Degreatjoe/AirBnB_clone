#!/usr/bin/python3
'''the amenity module'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
