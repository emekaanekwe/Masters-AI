'''
--CORE CONCEPTS OF OOP--

Class - allows for the creation of a more defined data strcture. Acts as a bueprint.

Method - the functions of the class that act as the "behaviors" that dictate class actions

Instance - a created object from the class that contains the "real" data

__init__ - sets the initial state of any instantiated object

Attributes - 
    instance attr = the params of the init.
    class att = defined vars that are global within class
 
Inheritance - 

Composition - 

Polymorphism - 


'''

class Bot:

    intellect = "Alas, this bot has yet to display true intelligence"

    # initial state with params (instance attributes)
    def __init__(self, id, name, active):
        # create attribute and assign the value of the parameter
        self.ver = "ver"
        self.id = id
        self.name = name
        self.active = active        
         
        
# instantiate class
b = Bot(1,3.566,3)
print(b.ver,b.id)