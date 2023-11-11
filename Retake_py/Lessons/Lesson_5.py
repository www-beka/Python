from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name, *args):
        self.name = name

    def __str__(self):
        return f"Transport name: {self.name}"

    @abstractmethod
    def get_info(self):
        raise NotImplementedError

class Vehicle(Transport):
    def __init__(self, name:str, marka:str, *args):
        super().init(name)
        self.marka = marka

    def __str__(self):
        return f"Vehicle marca: {self.marka}"

    @abstractmethod
    def get_info(self):
        raise NotImplementedError

class Truck(Vehicle):
    def __init__(self, name:str, marka:str, speed:int, color:str):
        super().init(name, marka)
        self.speed = speed
        self.color = color

    def get_info(self):
        return f"Transport type is Truck, name: {self.name}, marka: {self.marka}, speed: {self.speed}km/h, color: {self.color}"

class Car(Vehicle):
    def __init__(self, name:str, marka:str, speed:int, color:str):
        super().init(name, marka)
        self.speed = speed
        self.color = color

    def get_info(self):
        return f"Transport type is Car, name: {self.name}, marka: {self.marka}, speed: {self.speed}km/h, color: {self.color}"

truck = Truck("Dump", "MAN", 100, "Yellow")
car = Car("i8", "BMW", 320, "Red")

print(truck.get_info())
print(car.get_info())

#! --------------------------------------------------------------------------------------------------------------------------------

class Train(Transport):
    def __init__(self, name:str, marka:str, *args):
        super().init(name)
        self.marka = marka

    def __str__(self):
        return f"Vehicle marca: {self.marka}"

    @abstractmethod
    def get_info(self):
        raise NotImplementedError

class Intercity(Train):
    def __init__(self, name:str, marka:str, speed:int, color:str):
        super().init(name, marka)
        self.speed = speed
        self.color = color

    def get_info(self):
        return f"Transport type is Truck, name: {self.name}, marka: {self.marka}, speed: {self.speed}km/h, color: {self.color}"

class Tram(Train):
    def __init__(self, name:str, marka:str, speed:int, color:str):
        super().init(name, marka)
        self.speed = speed
        self.color = color

    def get_info(self):
        return f"Transport type is Car, name: {self.name}, marka: {self.marka}, speed: {self.speed}km/h, color: {self.color}"

poyezd = Intercity("AfroSiyob", "Afro", 500, "White and Blue-line")
tramvay = Intercity("MAroqand", "Sam", 250, "Blue and White-line")

print(poyezd.get_info())
print(tramvay.get_info())