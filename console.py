#!/usr/bin/python3
""" AirBnB clone - The console """

import cmd
import sys
from models import *


class HBNBCommand(cmd.Cmd):
    """ class consol """

    # change command prompt
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ quit: used to exit console """
        return True
    
    def do_EOF(self, args):
        """ EOF: used to mark End Of File """
        print()
        return True
    
    def do_creat(self, args):
        """ creat: used to creat user accounts"""
        print("User " + args + " created successfully")

    def precmd(self, cmdLine):
        """ 
            [!] This function is ran just before the command line is explicated
            Args:
                cmdLine (str): A command line inputed by user
            Return:
                command line ready to be executed
            Description:
                collect 'class name', 'command', 'id', and 'additional arguments '
                from the given command line after parcing
        """

        if ('.' in cmdLine):
            line = cmdLine.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            line = line.split(' ')
            line = f"{line[1]} {line[0]} {line[2]} {line[3]}"
            #print("Command Line: " + line)
            return line
        else:
            return cmdLine


if __name__ == '__main__':
    """ Our ∞ command loop"""
    HBNBCommand().cmdloop()