#!/usr/bin/python3
"""Defines hbnb command intepreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Sets up commands in command intepreter

    Args:
        prompt (str): prompt string stdout
        __classes (list): classes available
    """
    prompt = "(hbnb) "
    __classes = ['BaseModel',
                 'User',
                 'State',
                 'City',
                 'Place',
                 'Amenity',
                 'Review']

    def do_create(self, arg):
        """creates new instance of BaseModel
        saves it to JSON file
        prints the id
        Ex: (hbnb) create BaseModel
        """
        line = arg.strip()
        if line:
            if line in HBNBCommand.__classes:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints string representation of instance
        based on class name
        Ex: (hbnb) show BaseModel
        """
        model_name = model_id = ""
        args = arg.strip().split()
        objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            model_name = args[0]
        if len(args) == 1:
            print(print("** instance id missing **"))
            return
        else:
            model_id = args[1]
        if model_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif "{}.{}".format(model_name, model_id) not in objs:
            print("** no instance found **")
            return
        else:
            print(objs["{}.{}".format(model_name, model_id)])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        save changes to JSON file
        """
        line = arg.strip().split()
        model_name = model_id = ""
        objs = storage.all()

        if len(line) >= 1:
            model_name = line[0]
        else:
            print("** class name missing **")
            return
        if model_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(line) >= 2:
            model_id = line[1]
        else:
            print("** instance id missing **")
            return
        if "{}.{}".format(model_name, model_id) not in objs:
            print("** no instance found **")
            return
        else:
            del objs["{}.{}".format(model_name, model_id)]
            storage.save()

    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name
        Ex: $ all BaseModel or $ all
        """
        objs = storage.all().values()
        list = []

        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objs:
                if arg == obj.__class__.__name__:
                    list.append(obj.__str__())
                elif not arg:
                    list.append(obj.__str__())

            print(list)

    def do_update(self, arg):
        """adds or updates attribute to an instance
        saves changes to JSON file
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        model_name = model_id = attr_name = attr_val = ''
        args = arg.strip().split()
        objs = storage.all()

        if args:
            model_name = args[0]
        else:
            print("** class name missing **")
            return
        if model_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            model_id = args[1]
        else:
            print("** instance id missing **")
            return
        if len(args) >= 3:
            attr_name = args[2]
        else:
            print("** attribute name missing **")
            return
        if len(args) >= 4:
            attr_val = args[3]
        else:
            print("** value missing **")
            return
        try:
            my_obj = objs["{}.{}".format(model_name, model_id)]
            if attr_name in my_obj.__class__.__dict__.keys():
                valtype = type(my_obj.__class__.dict__[attr_name])
                my_obj.__dict__[attr_name] = valtype(attr_val.strip("\""))
            else:
                my_obj.__dict__[attr_name] = attr_val.strip("\"")
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_EOF(self, line):
        """command to exit program"""
        return True

    def do_quit(self, line):
        """command to exit program"""
        return True

    def emptyline(self):
        """defaults to doing nothing if no command provided"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
