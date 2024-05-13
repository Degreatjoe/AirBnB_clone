#!/usr/bin/python3
'''
A class  that serializes instances to a JSON file and
deserializes JSON file to instances
'''
import json
import os

class FileStorage:
    '''
    initializing of the filestorage class
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    serialized_objects = json.load(file)
                    for key, value in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                except:
                    pass
