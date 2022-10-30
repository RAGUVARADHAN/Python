from abc import ABC, abstractmethod
class character(ABC):
    def move(self):
        print('it will move')
    @abstractmethod
    def speak(self):
        print('it will speak')
class person():
    def move(self):
        print('Person can move')
c1=character()
c1.move()
p1=person()
p1.move()