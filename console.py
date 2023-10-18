#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0].split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg.split()[0]).id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance\n
        Based on the class name and id\n
        Ex: $ show BaseModel 1234-1234-1234
        """
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        if len(arg) == 1:
            print("** instance id missing **")
        elif arg:
            class_name = arg.split()[0]
            id = arg.split()[1]
        elif class_name not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        elif class_name + '.' + id not in obj.keys():
            print("** no instance found **")
        else:
            my_key = class_name + '.' + id
            my_dict = obj[my_key]
            print(my_dict)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id\n
        Saves changes into the JSON file)\n
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg:
            class_name = arg.split()[0]
            id = arg.split()[1]
        elif class_name not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        if class_name + '.' + id in obj.keys():
            my_key = class_name + '.' + id
            del obj[my_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances\n
        Based or not on the class name\n
        Ex: $ all BaseModel or $ all
        """
        my_class = arg.split()[0]
        objdict = storage.all()
        if len(arg) == 0:
            for value in objdict.values():
                print(value.to_dict())
        if my_class in HBNBCommand.__classes:
            for value in objdict.values():
                if value['__class__'] == my_class:
                    print(value.to_dict())
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id\n
        Adds or updates attribute\n
        Saves change into the JSON file\n
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        objdict = storage.all()
        if len(arg[0]) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not arg.split()[1]:
            print(" ** instance id missing **")
        elif not arg.split()[0] + '.' + arg.split()[1] not in objdict.keys():
            print("** no instance found **")
        elif not arg.split()[3]:
            print("** value missing **")
        elif arg:
            class_name = arg.split()[0]
            id_val = arg.split()[1]
            value = hasattr(objdict[class_name + '.' + id_val], arg.split()[2])
            if value is False:
                return False
            attrname = arg.split()[2]
            attrvalue = arg.split()[3]
            obj = objdict[arg.split()[0] + '.' + arg.split()[1]]
            if attrname in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.dict__[attrname])
                obj.__dict__[attrname] = valtype(attrvalue)
            else:
                obj.__dict__[attrname] = attrvalue
            storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
