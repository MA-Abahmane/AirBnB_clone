# AirBnB_clone
AirBnB clone - The console (ALx)
# AirBnB clone - The console (ALx)


The main goal of this project is to deploy on a server a simple copy of the AirBnB website. It won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

First step: Write a command interpreter to manage your AirBnB objects.
This first step is very important because it will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.


# What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object



# Execution
The consol works like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$



# Commands:
- create - create an object
- show - show an object (based on id)
- destroy - destroy an object
- all - show all objects, of one type or all types
- update - Updates an instance based on the class name and id
- quit/EOF - quit the console
- help - see descriptions of commands
- To start console type in shell



AirBnB_clone$ ./console.py
(hbnb) 

# Create
To create an object use format "create " ex:
    (hbnb) create BaseModel

# Show
To show an instance based on the class name and id. Ex:
    (hbnb) show BaseModel 1234-1234-1234.

# Destroy
To Delete an instance of an object use "destroy id". Ex:
(hbnb) destroy BaseModel 1234-1234-1234.

# All
all or all Ex:
(hbnb) all or all State

# Update
Updates an instance based on the class name and id:
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

# Quit
quit or EOF

# Help
help or help Ex:

(hbnb) help or help quit
Defines quit option


# Supported classes:
BaseModel
User
State
City
Amenity
Place
Review


# Authors
Mohamed Amine Abahmane - ma.abahmane@gmail.com