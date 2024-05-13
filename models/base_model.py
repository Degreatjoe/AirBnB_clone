#!/usr/bin/python3
'''
This is the Base class for my AirBnB project base_model.p
All other class will inherit from it.
'''
from datetime import datetime
import uuid


class BaseModel:
    '''
    Initializing the basemodel class
    '''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        the __str__ function to return a string
        '''
        return (f"[{self.__class__.name}] [{self.id}] {self.__dict__}")

    def save(self):
        '''
        The save method which will save the update time
        '''
        self.update_atm = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
