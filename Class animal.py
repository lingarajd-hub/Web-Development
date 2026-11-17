from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
R = Human()
R.move()
K = Snake()
K.move()
S = Dog()
S.move()
J = Lion()
J.move()