#!/usr/bin/python3
"""doc doc"""
import cmd


class HBNBCommand(cmd.Cmd):
    """dooooocks"""
    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        """dooc dooc doick"""
        return True

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
