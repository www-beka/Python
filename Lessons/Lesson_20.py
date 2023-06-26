from abc import ABC, abstractmethod

# class AbcAnimal(ABC):
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food

#     @abstractmethod
#     def get_decription(self):
#         raise NotImplementedError
    

# class Pets(AbcAnimal):
#     def __init__(self, name, food, speed):
#         super().__init__(name, food)
#         self.speed = speed
    
#     def get_decription(self):
#         return f"{self.name} eats {self.food}"
    

# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_decription())


class AbcTransport(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def move():
        pass


class Vehcie(AbcTransport):
    def __init__(self):
        pass

class Truck(Vehcie):
    def __init__(self):
        pass
class Car(Vehcie):
    def __init__(self):
        pass



class Train(AbcTransport):
    def __init__(self):
        pass

class Poyezd(Train):
    def __init__(self):
        pass

class Tranvay(Train):
    def __init__(self):
        pass

