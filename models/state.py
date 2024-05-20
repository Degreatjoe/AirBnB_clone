#!/usr/bin/python3
'''
the state Module to handle the state
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    the state class
    '''
    def __init__(self, *args, **kwargs):
        '''initializing the state instance'''
        super().__init__(*args, **kwargs)
        self.name = ""
