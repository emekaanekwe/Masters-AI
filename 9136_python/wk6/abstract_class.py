from abc import ABC, abstractmethod

class Ghost(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def ghost_name(self) -> str:
        print("there is a ghost here, and it's abstract")
        return self.name

test = Ghost
print(test.ghost_name("banshee"))