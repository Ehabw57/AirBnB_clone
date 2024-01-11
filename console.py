#!/usr/bin/python3
"""doc doc"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


classes = {
        "basemodel": BaseModel,
        "user": User,
        "city": City,
        "place": Place,
        "state": State,
        "review": Review,
        "amenity": Amenity
        }


def extract_val(val):
    """git push"""
    try:
        val = val.split('"')[1]
        if '.' in val:
            return float(val)
        return int(val)
    except (IndexError, ValueError):
        return val


def get_by_id(class_name, id):
    """dooooocks"""
    key = f'{class_name.lower()}'
    key = f"{classes[key].__name__}.{id}"
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
    prompt = "(hbnb) "

    def do_all(self, arg):
        """Usage: all [class]\nshow all instances of the class, or just all"""
        instance_list = []
        if arg == "":
            instance_list = [str(val) for val in storage.all().values()]
            print(instance_list)
            return
        if class_check(arg):
            for value in storage.all().values():
                if arg.lower() == value.__class__.__name__.lower():
                    instance_list.append(str(value))
            print(instance_list)

    def do_create(self, arg):
        """usage: create <class>\ncreate an instance of the class"""
        if class_check(arg):
            instance = classes[arg.lower()]()
            print(instance.id)
            storage.save()

    def do_destroy(self, arg):
        """Usage: destroy <class><instance id>\nDelete the instance of class"""
        args = arg.split() + ['', '']
        if class_check(args[0]):
            instance = get_by_id(args[0], args[1])
            if instance:
                storage.delete(instance)
                storage.save()

    def do_show(self, arg):
        """usage: show <class> <id>\nget informations about an instance"""
        args = arg.split() + ['', '']
        if class_check(args[0]):
            instance = get_by_id(args[0], args[1])
            instance and print(instance)

    def do_update(self, arg):
        """Usage: all [class]\nshow all instances of the class, or just all"""
        args = arg.split(" ", 3) + ["", "", "", ""]
        class_name, id, attr, new_val = args[:4]
        new_val = extract_val(new_val)
        if class_check(class_name) and (instance := get_by_id(class_name, id)):
            if attr == "":
                print("** attribute name missing **")
            elif new_val == "":
                print("** value missing **")
            else:
                setattr(instance, attr, new_val)
                instance.save()

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
