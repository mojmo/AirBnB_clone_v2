#!/usr/bin/python3
""""""
import cmd
import re

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """"""

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
        """
        Command to exit the command loop.
        """
        return True

    def do_EOF(self, line):
        """
        Signal to exit the command loop.
        """
        print()
        return True

    def emptyline(self):
        """
        Override the default behavior for an empty line (do nothing).
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class.
        """
        arg = arg.strip()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            storage.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Display information about a specific instance.
        """
        line = line.strip()
        args = line.split(' ')
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
        """
        line = line.strip()
        args = line.split(' ')
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
        """
        List all instances or instances of a specific class.
        """
        arg = arg.strip()
        objects_dict = storage.all()
        objects_list = [f"{val}" for val in objects_dict.values()]
        if len(arg) == 0:
            print(objects_list)
        elif arg not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        else:
            cls_objects = []
            for obj in objects_dict.values():
                if obj.__class__.__name__ == arg:
                    cls_objects.append(obj.__str__())
            print(cls_objects)

    def do_update(self, line):
        """
        Update the attributes of a specified instance.
        """
        line = line.strip()
        args = line.split(' ')
        objects_dict = storage.all()

        if len(args) == 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects_dict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            updated_obj = objects_dict[f'{args[0]}.{args[1]}']
            # If the updated argument is new
            if args[2] in updated_obj.__class__.__dict__.keys():
                value_type = type(updated_obj.__class__.__dict__[args[2]])
                updated_obj.__dict__[args[2]] = value_type(args[3])
            else:
                updated_obj.__dict__[args[2]] = args[3]

            storage.save()

    def do_count(self, line):
        """
        Count the number of instances of a specified class.
        """

        line = line.strip()
        args = line.split(' ')
        objects_dict = storage.all()
        count = 0

        for obj in objects_dict.values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """
        Handle unknown commands based on defined patterns.
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
                args = re.sub("[\"\',]", "", args)
                args = f"{cls_name} " + args

                return methods[method_name](args)

        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
