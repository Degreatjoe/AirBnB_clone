#!/usr/bin/python3
'''the cuty module'''
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    def __init__(self, *args, **kwargs):
        """Initializes City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
