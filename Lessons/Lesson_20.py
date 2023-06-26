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



lesson = "Class  &&  OOP"
# Abstract
# Inheritance

# this == self

# class User:
#     def __init__(self, name):
#         print(f"User {name} is created")
#         self.name = name

# user1 = User("John")
# print(user1)
# print(user1.name)


# __init__  => is a constructor method which is used to initialize the attributes of a class
# it is called automatically when an object is created

#############################################################################################
################ Abstraction

# "abc" here stands for abstract base class. It is first imported and then used as 
# a parent class for some class that becomes an abstract class. Its simplest implementation 
# can be done as below.


from abc import ABC, abstractmethod
class AbcAnimal(ABC):
    def __init__(self, name, food):
        self.name = name
        self.food = food

    @abstractmethod
    def get_description(self):
        pass
        # raise NotImplementedError


class Pets(AbcAnimal):
    def __init__(self, name, food, speed):
        super().__init__(name, food)
        self.speed = speed

    def get_description(self):
        return f"{self.name} eats {self.food}"


# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_description())



# abs module is used to create abstract classes
# it is helpful when we want to create a class that will be used as a base class
# abstractmethod is used to declare abstract methods which will be implemented by the child classes
# is it used to ensure that the child classes will have the same method as the parent class
# and returns an error if the child class does not have the same method as the parent class
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.

#############################################################################################
################ Inheritence

# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).

class Parent:
    def __init__(self, name):
        self.name = name
    
    def test(self):
        print("Hello world")

class Child(Parent, ABC):
#     Inherited members from parent class
#     Additional members of the child class
    def __init__(self, name, age):
        super().__init__(name)  # => calls the parent class constructor
        self.age = age

    def test(self):
        print("Hello world from child")

    def __repr__(self) -> str:
        """
            Is used to represent the object with a string.
            It is used for debugging and logging.
        """
        return f"{self.name} is {self.age} years old"

    def __str__(self) -> str:
        """
            Is used to represent the object with a string.
            It is used for the end user.
        """
        return f"{self.name} is {self.age} years old"


child = Child("John", 20)
print(child)
print(child.test())