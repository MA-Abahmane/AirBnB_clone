#!/usr/bin/python3
""" AirBnB clone - The console """

import cmd
import sys
from models import *


class console(cmd.Cmd):
    """ class consol """

    # change command prompt
    prompt = '(AIR_bnb)>> '

    def do_exit(self, args):
        """ exit console """
        return True
    
    def do_creat(self, args):
        """ creat User """
        print("User " + args + " created successfully")


    def do_print(self, args):
        """ print 7 times """
        print(f"{args}\t" * 7)


    def precmd(self, cmdLine):
        """ 
            [!] This function is ran just before the command line is explicated
            Args:
                cmdLine (str): A command line inputed by user
            Return:
                command line ready to be executed
            Description:
                check in what mode the command line is inputed (consol or piped) 
                parse if the command line has more than one arguments
                if not, run command
        """
        args = cmdLine.split('.', 1)
        if (len(args) == 2):
            Class = args[0] #  given class name acquired
            args = args[1].split('(', 1)
            Cmnd = args[0] #  user command acquired
            if (len(args) == 2):
                args = args[1].split(')', 1)
                if (len(args) == 2):
                    Id = args[0] # class id acquired
                    Other = args[1] # other additional arguments
            parsed_cmdL = Cmnd + ' ' + Class + ' ' + Id + ' ' + Other
            return parsed_cmdL
        else:
            return cmdLine


if __name__ == '__main__':
    """ ∞ loop """
    console().cmdloop() # type: ignore
