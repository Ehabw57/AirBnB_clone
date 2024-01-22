# AirBnB

A fullstack web application using Python, HTML, CSS, JavaScript.

## The Console

A command interpreter to administrate/manage the AirBnB storage and objects, written in Python.

#### How it works?

After cloning the repository in your host machine run the console.py script

```sh
$ python3 AirBnB_clone/console.py
```

An interactive prompt will appear with the label `(hbnb)`, now you can start doing *CRUD* operations by commanding `(hbnb)`.

to see all the available commands type `help`:

```hbnb
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```


to see how to use a specific command type `help <command>`:

```hbnb
(hbnb) help create
usage: create <class>
create an instance of the class
(hbnb)
```


For example, to create a new User instence:
```hbnb
(hbnb) create User
```

available classes are `User`, `Place`, `City`, `State`, `Review`, `Amenity`:

the reply for the last command we gave to `(hbnb)` was:
```hbnb
(hbnb) create User
2e73b834-97cb-4ba9-bc7a-06c95fd84585
(hbnb)
```

now we have an ID for the new user, we can add other properties using `update`:
```hbnb
(hbnb) show user 2e73b834-97cb-4ba9-bc7a-06c95fd84585
[User] (2e73b834-97cb-4ba9-bc7a-06c95fd84585) {'id': '2e73b834-97cb-4ba9-bc7a-06c95fd84585', 'created_at': datetime.datetime(2024, 1, 22, 16, 17, 28, 404795), 'updated_at': datetime.datetime(2024, 1, 22, 16, 17, 28, 404795)}
(hbnb) update user 2e73b834-97cb-4ba9-bc7a-06c95fd84585 name Mohammed
(hbnb) update user 2e73b834-97cb-4ba9-bc7a-06c95fd84585 email "mohammed123@mail.com"
(hbnb) show user 2e73b834-97cb-4ba9-bc7a-06c95fd84585
[User] (2e73b834-97cb-4ba9-bc7a-06c95fd84585) {'id': '2e73b834-97cb-4ba9-bc7a-06c95fd84585', 'created_at': datetime.datetime(2024, 1, 22, 16, 17, 28, 404795), 'updated_at': datetime.datetime(2024, 1, 22, 16, 22, 21, 674695), 'name': 'Mohammed', 'email': 'mohammed123@mail.com'}
```

and so on we can create other objects, read their properties, update some properties, and delete objects, and that what we refered to with the CRUD operations above.
