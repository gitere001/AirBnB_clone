#!/usr/bin/python3
"""A module with HBNBCommand(cmd.Cmd) class"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A command-line interpreter for the AirBnb clone - console project.

    This class provides a command-line interface for interacting with the
    AirBnb clone project. It supports various commands for creating,
    displaying, updating, and deleting instances of different classes.

    Attributes:
        prompt (str): The prompt displayed in the command-line interface.

    Methods:
        emptyline(): Overrides the default behavior when an empty line is
        entered.
        do_quit(arg): Quits the current session.
        help_quit(): Prints help information for the quit command.
        do_EOF(arg): Handles EndOfFile (Ctrl+D) to exit the program.
        do_create(arg): Creates a new instance of a specified class.
        do_show(arg): Displays the string representation of a specified
        instance.
        do_destroy(arg): Deletes an instance based on the class name and ID.
        do_all(arg): Prints string representations of all instances or
        specific class instances.
        do_update(arg): Updates attributes of an instance based on the class
        name and ID.

    Usage:
        - Run the program to start the command-line interface.
        - Enter commands at the prompt to interact with the AirBnb clone
        project.
    """
    prompt = "(hbnb)"
    class_exists = ["BaseModel", "User", "Place", "Review", "City", "Amenity",
                    "State"]

    def emptyline(self):
        """Do nothing whenever an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quits the current session"""
        return True

    def help_quit(self):
        """Print help for quit command."""
        print("Quit command to exit the program.")

    def do_EOF(self, arg):
        """
        Handles EndOfFile(ctrl+D), exits the program
        """
        print()  # print a new line
        return True

    def do_create(self, arg):
        """
        Create a new instance and save it to a JSON file.

        Usage: create <class_name>

        Description:
            Creates a new instance of the specified class and saves it to a
            JSON file.
        """
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in self.class_exists:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{cmnds[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.

        Usage: show <class_name> <class_id>

        Description:
            Shows the string representation of the instance identified by the
            specified class name and ID.
        """
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in self.class_exists:
            print("** class doesn't exist **")
        elif len(cmnds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = f"{cmnds[0]}.{cmnds[1]}"
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance by class name and ID.

        Usage: destroy <class_name> <class_id>

        Description:
            Deletes the instance identified by the specified class name and ID.
        """
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            print("** class name missing **")
            return
        if cmnds[0] not in self.class_exists:
            print("** class doesn't exist **")
            return
        elif len(cmnds) < 2:
            print("** instance id missing **")
            return
        else:
            objs = storage.all()
            key = f"{cmnds[0]}.{cmnds[1]}"
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print all instances or instances of a specific class.

        Usage: all [class_name]

        Description:
            Prints string representations of all instances if no class name is
            provided.
            If a class name is provided, prints string representations of
            instances
            belonging to that class.
        """
        all_objs = storage.all()
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            for key, value in all_objs.items():
                print(str(value))
        elif cmnds[0] not in self.class_exists:
            print("** class doesn't exist **")
        else:
            for key, value in all_objs.items():
                if key.split(".")[0] == cmnds[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Update an instance attribute.

        Usage: update <class_name> <class_id> <attribute_name>
        "<attribute_value>"

        Description:
            Updates the attribute of an instance specified by its class name
            and ID.
            The attribute name and value should be provided in the correct
            order.
            If the attribute value contains spaces, enclose it in double
            quotes.
        """
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in self.class_exists:
            print("** class doesn't exist **")
        elif len(cmnds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = f"{cmnds[0]}.{cmnds[1]}"
            if key not in objs:
                print("** no instance found **")
            elif len(cmnds) < 3:
                print("** attribute name missing **")
            elif len(cmnds) < 4:
                print("** value missing **")
            else:
                obj = objs[key]
                attr_name = cmnds[2]
                attr_value = cmnds[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
