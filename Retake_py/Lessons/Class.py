class Animals:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError
    
class Dog(Animals):
    def speak(self):
        return self.name+' says woolf'
    
class Cat(Animals):
    def speak(self):
        return self.name+' says meow'

from datetime import date

class Student:
    def __init__(self, name, age) -> None: 
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age > 18
        
student_1 = Student('Javani', 19)
student_2 = Student.fromBirthYear('Anna', 1994)


print(student_1.age)
print(student_2.age)