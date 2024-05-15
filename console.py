#!/usr/bin/python3
"""
Console Module
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


ALLOWED_CLASSES = ['BaseModel', 'User']
class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a model class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        #check if the class exist in our storage
        if class_name not in ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = arg.split()[0]
            if class_name not in ALLOWED_CLASSES:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items() if key.split('.')[0] == class_name])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        storage.save()

    def emptyline(self):
        '''Do nothing when an empty line is entered
        '''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
