from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    @abstractmethod
    def see(self):
        pass