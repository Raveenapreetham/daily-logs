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

objs=[Bike(), Car()]
for a in objs:
    print(a.start_engine())

