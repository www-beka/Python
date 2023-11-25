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
        
# student_1 = Student('Javani', 19)
# student_2 = Student.fromBirthYear('Anna', 1994)


# print(student_1.age)
# print(student_2.age)

# import time, math

# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print('Total time take in: ', func.__name__, end - begin)
#     return inner1

# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

# memory = {}

# def memorize_factorial(orig_func):
#     def inner(num):
#         if num not in memory:
#             memory[num] = orig_func(num)
#             print('Saved to memory')
#         else:
#             print('From saved memory: ', memory[num])
#         return memory[num]
#     return inner
# @memorize_factorial
# def faccto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * faccto(num - 1)

# print(faccto(5))
# print(faccto(4))
# print(memory)


# def decorator_fn(fn):
#     def inner(string):
#         print(f'string name', fn(string))
#     return inner

# @decorator_fn
# def test_fn2(string):
#     return string

# test_fn2('Test-tests')

def chek_input(fn):
    def inner(string):
        if type(fn(string)) == int:
            print('Correct')
        elif type(fn(string)) == str:
            print('Correct')
        else:
            print('Inveled input tupe') 
    return inner

@chek_input
def get_text(string):
    return string

get_text(123.5)