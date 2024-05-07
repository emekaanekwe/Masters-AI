'''ABSTRACT CLASSES & METHODS'''
#

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
             
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)





class Abst(ABC):
    def __init__(self):
        self.one = 1
        self.str = "str"
    
    @abstractmethod
    def override(self):
        print("abstract method")

class Bot1(Abst):
    def override(self):
        print("bot 1 made")

class Bot2(Abst):
    def override(self):
        print("bot 2 made")
    
bot1 = Bot1()
bot2 = Bot2()
#does not reach
bot1.override()
#does not reach
bot2.override()



class A:
    def m1(self):
        print("m1")
    def m2(self):
        print("m2")
class B(A):
    #there is no direct inheritance
    def m1(self):
        print("m1.1")
    def m3(self):
        print("m3")

x = A()
y = B()
x.m1()
y.m3()
y.m1()

class Bots:
    def __init__(self, name):
        self.name = name
    def check(self):
        print(self.name)

class Host(Bots):
    def __init__(self):
        self.alive = True
        super().__init__()
    def isalive(self):
        print("is it alive?", self.alive)
    def isname(self):
        print(f"it's name is {self.name}")    




'''
class Post(ABC):
    """ Abstract Post class for representing and manipulating posts. """

    caption = "" # Class Variable.

    def __init__(self, image): # Constructor (with parameters).
        """ Create a new post. """
        self.image = image
        self.caption = self.caption
        self.reactions = []

    # Methods
    def get_caption(self):
        return self.caption

    def get_image(self):
        return self.image

    def get_reactions(self):
        return self.reactions

    def set_caption(self, caption):
        self.caption = caption

    def set_image(self, image):
        self.image = image

    @abstractmethod
    def update_reactions(self, index):
        pass

    @abstractmethod
    def __str__(self): # Overrides the __str__ method.
        pass

class InstaOuncePost(Post):

    def __init__(self, image):
        super().__init__(image)
        self.reactions.append(0)

    def update_reactions(self, index=0):
        self.reactions[index] += 1 # Only 'Likes' are allowed as a reaction.

    def __str__(self): # Overrides the __str__ method.
        return "Image directory = {}, Caption = {}, Likes = {}".format(self.image, self.caption, self.reactions[0])

class ChirperPost(InstaOuncePost):

    def get_caption(self):
        return super().get_caption()[:40] # Only allowed the first 40 characters.

class HeadBookPost(Post):
    
    def __init__(self, image):
        super().__init__(image)
        for i in range(3): # Assume there are only three different reactions (e.g., Like, Heart and Thumb Down)
            self.reactions.append(0)

    def update_reactions(self, index):
        self.reactions[index] += 1

    def __str__(self): # Overrides the __str__ method.
        return "Image directory = {}, Caption = {}, Reactions = {}".format(self.image, self.caption, self.reactions)


io_post = InstaOuncePost("io_image.jpg") # Instantiation of a new InstaOuncePost object.
print(io_post)
# Prints: 'Image directory = io_image.jpg, Caption = , Likes = 0'

ch_post = ChirperPost("ch_image.jpg") # Instantiation of a new ChirperPost object.
print(ch_post)
# Prints: 'Image directory = ch_image.jpg, Caption = , Likes = 0'

h_post = HeadBookPost("h_image.jpg") # Instantiation of a new HeadBookPost object.
print(h_post)
# Prints: 'Image directory = h_image.jpg, Caption = , Reactions = [0, 0, 0]'

io_post.update_reactions()
print(io_post)
# Prints: 'Image directory = io_image.jpg, Caption = , Likes = 1'

ch_post.update_reactions()
print(ch_post)
# Prints: 'Image directory = ch_image.jpg, Caption = , Likes = 1'

h_post.update_reactions(1)
print(h_post)
# Prints: 'Image directory = h_image.jpg, Caption = , Reactions = [0, 1, 0]'

ch_post.set_caption('Let me share with you about that one day when we went to a music festival in Montreal, Quebec, Canada. You see, Osheaga is one of the biggest music festivals in North America that attracts so many big names from all around the world!')
print(ch_post.get_caption())
# Prints: 'Let me share with you about that one day'
'''