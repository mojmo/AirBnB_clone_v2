#!/usr/bin/python3
"""
Provides a command-line interface for interacting with
storage and data models.
"""
import cmd
import re

from models import storage
from models.engine.file_storage import get_class_name_to_class
from shlex import split


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
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class.
        """
        args = parse_command(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        else:
            class_name_to_class = get_class_name_to_class()
            cls = class_name_to_class[args[0]]
            new_model = cls()
            storage.save()
            print(new_model.id)

    def do_show(self, line):
        """Display information about a specific instance.
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
        """Remove a specified instance.
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
        """List all instances or instances of a specific class.
        """
        args = parse_command(arg)
        objects_dict = storage.all()
        objects_list = [f"{val}" for val in objects_dict.values()]
        if len(args) == 0:
            print(objects_list)
        elif args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        else:
            cls_objects = []
            for obj in objects_dict.values():
                if obj.__class__.__name__ == args[0]:
                    cls_objects.append(obj.__str__())
            print(cls_objects)

    def do_update(self, line):
        """Update the attributes of a specified instance.
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
        """Count the number of instances of a specified class.
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
