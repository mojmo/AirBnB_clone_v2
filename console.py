#!/usr/bin/python3
"""
Provides a command-line interface for interacting with
storage and data models.
"""
import cmd
import re

import models
from models import storage
from models.engine.file_storage import get_class_name_to_class

import shlex  # for splitting the line along spaces except in double quotes
from shlex import split

import cmd
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


def parse_command(command):

    dict_arg = re.search(r'\{(.*?)\}', command)
    list_arg = re.search(r'\{(.*?)\}', command)

    if dict_arg is None:
        if list_arg is None:
            return [arg.strip(',') for arg in split(command)]
        else:
            tokens_before_list = split(command[:list_arg.start()])
            parsed = [token.strip(',') for token in tokens_before_list]
            parsed = parsed + [list_arg.group()]
            return parsed
    else:
        tokens_before_dict = split(command[:dict_arg.start()])
        parsed = [token.strip(',') for token in tokens_before_dict]
        parsed = parsed + [dict_arg.group()]
        return parsed


class HBNBCommand(cmd.Cmd):
    """Command-line interface for managing data models and storage."""

    prompt = '(hbnb) '

    defined_classes = [
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
    ]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Signal to exit the command loop.
        """
        print()
        return True

    def emptyline(self):
        """Override the default behavior for an empty line (do nothing).
        """
        return False

    def do_create(self, arg):
        """
        Create a new instance of a specified class, with optional initialization parameters.
        USAGE: create <class name> <param 1> <param 2> <param 3>...
        Param syntax: <key name>=<value>
        """
        args = shlex.split(arg)  # Use shlex.split to correctly handle spaces within quotes
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
            return

        # Create an instance of the class
        new_instance = classes[class_name]()

        # Iterate over additional arguments to set attributes on the object
        for param in args[1:]:
            key, value_str = param.split("=", 1)
            # Detect and preserve string values correctly
            if value_str.startswith('"') and value_str.endswith('"'):
                # Handle strings explicitly, including internal quotes and underscores
                value = value_str[1:-1].replace('\\"', '"').replace('_', ' ')
            elif value_str.isdigit() and (key == 'city_id' or key == 'user_id'):
                # Preserve city_id and user_id as strings explicitly
                value = value_str
            elif '.' in value_str:
                try:
                    value = float(value_str)
                except ValueError:
                    print(f"Error: {value_str} is not a valid float. Skipping...")
                    continue
            else:
                try:
                    value = int(value_str)
                except ValueError:
                    # Treat as a string if it's not a valid number
                    value = value_str.replace('_', ' ')

            # Set the attribute on the instance
            setattr(new_instance, key, value)

        storage.new(new_instance)
        storage.save()
        print(new_instance.id)



    def do_show(self, line):
        """
        Display information about a specific instance.
        USAGE: show <class name> <id>
        """
        args = parse_command(line)
        objects_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict[f'{args[0]}.{args[1]}'])

    def do_destroy(self, line):
        """
        Remove a specified instance.
        USAGE: show <class name> <id>
        """
        args = parse_command(line)
        objects_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects_dict:
            print("** no instance found **")
        else:
            del objects_dict[f'{args[0]}.{args[1]}']
            storage.save()

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, line):
        """
        Update the attributes of a specified instance.
        USAGE: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = parse_command(line)
        objects_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if f'{args[0]}.{args[1]}' not in objects_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return
        if len(args) == 4:
            updated_obj = objects_dict[f'{args[0]}.{args[1]}']
            # If the updated argument is new
            if args[2] in updated_obj.__class__.__dict__.keys():
                value_type = type(updated_obj.__class__.__dict__[args[2]])
                updated_obj.__dict__[args[2]] = value_type(args[3])
            else:
                updated_obj.__dict__[args[2]] = args[3]

            storage.save()
        elif type(eval(args[2])) == dict:
            updated_obj = objects_dict[f'{args[0]}.{args[1]}']

            for key, val in eval(args[2]).items():
                if (key in updated_obj.__class__.__dict__.keys() and
                    type(updated_obj.__class__.__dict__[key] in
                         [str, int, float])):
                    value_type = type(updated_obj.__class__.__dict__[key])
                    updated_obj.__dict__[key] = value_type(val)
                else:
                    updated_obj.__dict__[key] = val

            storage.save()

    def do_count(self, line):
        """
        Count the number of instances of a specified class.
        USAGE: count <class name>
        """
        args = parse_command(line)
        objects_dict = storage.all()
        count = 0

        for obj in objects_dict.values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """Handle unknown commands based on defined patterns.
        """

        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        split_command = re.search(r'(\w+).?(.+)', line)

        if split_command is not None:
            cls_name = split_command.group(1)
            match_method = re.search(r'(\w+)\((.*)\)', line)

            if (cls_name in HBNBCommand.defined_classes and
                    match_method is not None):
                method_name = match_method.group(1)
                args = match_method.group(2)
                # args = re.sub("[\"\',]", "", args)
                args = f"{cls_name} " + args

                return methods[method_name](args)

        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
