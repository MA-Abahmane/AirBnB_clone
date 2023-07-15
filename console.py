#!/usr/bin/python3
""" AirBnB clone - The console """

import cmd
import sys
import shlex as sx
import models
from models.base_model import *
from models.user import *
from models.state import *
from models.city import *
from models.amenity import *
from models.place import *
from models.review import *


class HBNBCommand(cmd.Cmd):
    """ class consol """

    # change command prompt
    prompt = '(hbnb) '

    # all classes we have
    class_list = {'BaseModel': BaseModel,
                  'User': User,
                  'State': State,
                  'City': City,
                  'Amenity': Amenity,
                  'Place': Place,
                  'Review': Review
                  }

    def emptyline(self):
        """ incase of emptyline input """
        pass

    def do_EOF(self, args):
        """ EOF: used to mark End Of File """
        print()
        return True

    def do_quit(self, args):
        """ quit: used to exit console """
        return True

    def do_create(self, args):
        """
            creat: used to creat a new instance of a given class
            Usage: create <class name>
        """
        # check if class name exists
        if (args):
            # check if class name is registered
            if (args in self.class_list):
                # creat instance of given class
                className = eval(args)
                obj = className()
                print(obj.id)
                # Update/save to JSON file
                models.storage.save()
            else:
                return print("** class doesn't exist **")
        else:
            return print("** class name missing **")

    def do_all(self, args):
        """ all: used to prints all string representation of
            all instances based or not on the class name.
            Usage: all <class name> or all
        """
        obj_list = []
        line = sx.split(args)
        obj_dict = models.storage.all()

        # [all] print all instances string representation after listing it
        if (len(line) == 0):
            for key in obj_dict.keys():
                obj_list.append(str(obj_dict[key]))
            print(obj_list)

        # [all <class name>] print all instances of given class name after
        # saving it to a list
        else:
            if (line[0] in self.class_list):
                for key in obj_dict.keys():
                    Skey = key.split('.')
                    # match class names and save in list
                    if (Skey[0] == line[0]):
                        obj_list.append(str(obj_dict[key]))
                print(obj_list)

            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
            show: used to prints the string representation
            of an instance based on the class name and id
            Usage: show <class name> <id>
        """
        line = sx.split(args)
        if (len(line) == 0):
            print("** class name missing **")
            return
        if (len(line) == 1):
            print("** instance id missing **")
            return
        if (not line[0] in self.class_list):
            print("** class doesn't exist **")
            return

        # load Database and build object key for the search
        obj_dict = models.storage.all()
        obj_key = f"{line[0]}.{line[1]}"

        # instance seach; print instance if found
        for key in obj_dict.keys():
            if (key == obj_key):
                print(obj_dict[key])
                return
        # instance not found
        print("** no instance found **")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
            Usage: destroy <class name> <id>
        """
        line = sx.split(args)
        # missing class name
        if (len(line) == 0):
            print("** class name missing **")
            return
        # if id is missing
        if (len(line) == 1):
            print("** instance id missing **")
            return
        # if given class name is unknown
        if (line[0] in self.class_list):
            # import database and build object key
            obj_dict = models.storage.all()
            obj_key = f"{line[0]}.{line[1]}"

            # search and delete
            for key in obj_dict.keys():
                if (key == obj_key):
                    del obj_dict[obj_key]
                    models.storage.save()
                    return
            print("** no instance found **")
        # given class is incorrect
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute
            Usage: update <class name> <id> <attribute name> "<value>"
        """
        line = sx.split(args)
        # if class name is missing
        if (len(line) == 0):
            print("** class name missing **")
            return
        # if id is missing
        if (len(line) == 1):
            print("** instance id missing **")
            return
        # if attribute name is missing
        if (len(line) == 2):
            print("** attribute name missing **")
            return
        # if attribute value is missing
        if (len(line) == 3):
            print("** value missing **")
            return

        # if class name is unknown
        if (line[0] in self.class_list):
            obj_dict = models.storage.all()
            obj_key = f"{line[0]}.{line[1]}"

            # get instance is it exists
            if (obj_key in obj_dict):
                instance = obj_dict[obj_key]
            else:
                print("** no instance found **")
                return

            # check is attribute exists. if NO; pass and set attribute
            # if YES; get attribute type, convert to its type and save
            try:
                attr_type = type(getattr(instance, line[2]))
                line[3] = attr_type(line[3])
            except AttributeError:
                pass
            # Update/set attribute and update JSON file
            setattr(instance, line[2], line[3])
            models.storage.save()

        else:
            print("** class doesn't exist **")

    def do_count(self, args):
        """
            count: used to retrieve the number of instances of a class
            Usage: <class name>.count() or count <class name>
        """
        count = 0
        obj_dict = models.storage.all()
        for key in obj_dict.keys():
            Skey = key.split('.')
            if (Skey[0] == args):
                count += 1
        print(count)

    def precmd(self, cmdLine):
        """
            [!] This function is ran just before the command line is intepreted
            Args:
                cmdLine (str): A command line inputed by user
            Return:
                command line ready to be executed
            Description:
                collect 'class name', 'command', 'id', and 'additional
                arguments' from the given command line after parcing
        """
        # this is 'update's special command parser, input format:
        # <class name>.update(<id>, <attribute name>, <attribute value>).
        if ('.' in cmdLine):
            line = cmdLine.replace('.', ' ').replace('(', ' ')
            line = line.split(' ')
            if (line[1] == 'update'):
                line = cmdLine.replace('.', ' ').replace('(', ' ').\
                replace(', ', ' ').replace(',', ' ').replace(')', ' ')

                line = line.split(' ')
                line = f"{line[1]} {line[0]} {line[2]} {line[3]} {line[4]}"
                print (" Update line: " + line)
                return line

        # parse other special commands
        Llen = sx.split(cmdLine)
        if ('.' in cmdLine and len(Llen) == 1):
                line = cmdLine.replace('.', ' ').replace('(', ' ').\
                    replace(')', ' ')

                line = line.split(' ')
                line = f"{line[1]} {line[0]} {line[2]} {line[3]}"
                print("Command Line: " + line)
                return line

        return cmdLine


if __name__ == '__main__':
    """ Our ∞ command loop"""
    HBNBCommand().cmdloop()
