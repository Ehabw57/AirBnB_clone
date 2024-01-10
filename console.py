#!/usr/bin/python3
"""doc doc"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user_model import User

classes = {
        "basemodel": BaseModel,
        "user": User
        }

def get_by_id(class_name, id):
    """dooooocks"""
    key = f'{class_name}.{id}'
    if id == "":
        print("** instance id missing **")
    elif key not in storage.all().keys():
        print("** no instance found **")
    else:
        return storage.all()[key]



def class_check(arg):
    """dooooocks"""
    if arg == "":
        print("** class name missing **")
    elif arg.lower() not in classes.keys():
        print("** class doesn't exist**")
    else:
        return True


class HBNBCommand(cmd.Cmd):
    """dooooocks"""
    prompt = "(hbnb)"
    
    def do_create(self, arg):
        """usage: create <class>\ncreate an instance of the class"""
        if cmd_check(arg):
            instance = classes[arg.lower()]()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """usage: show <class> <id>\nget informations about an instance"""
        args = arg.split() + ['', '']
        if class_check(args[0]):
            instance = get_by_id(args[0], args[1])
            instance and print(instance)


    def do_quit(self, arg):
        """usage: quit\nexit the console"""
        return True

    def do_EOF(self, arg):
        """usage: <Ctrl-d>\nexit the console"""
        print()
        return True

    def emptyline(self):
        """handle empty input"""
        pass

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
