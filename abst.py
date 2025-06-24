from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Bike(Vehicle):

    def start_engine(self):
        return "engine started"


class Car(Vehicle):

    def start_engine(self):
        return "engine started"


obj=Bike()
print(obj.start_engine())

obj2=Car()
print(obj2.start_engine())





