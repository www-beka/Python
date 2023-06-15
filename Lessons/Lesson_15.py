# isinstance()  Returns True if a specified object is an instance of a specified object
#           RU: Возвращает True, если указанный объект является экземпляром указанного объекта
# EX:
# print(type(123) == str)
# print(isinstance(5, str))

# ------------------------------------------------------------------------------
# issubclass()  Returns True if a specified class is a subclass of a specified object
#           RU: Возвращает True, если указанный класс является подклассом указанного объекта
#           EX:
#               class Person:
#                   name = 'John'
#                   age = 36
#               
#               class Student(Person):
#                   grade = 9
#
#               x = issubclass(Student, Person)
# ------------------------------------------------------------------------------
# iter()      Returns an iterator object
#           RU: Возвращает объект итератора
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
#               print(next(x))  =>  cherry
#               print(next(x))  =>  StopIteration


# # iteration   =>  итерация (проход по элементам коллекции)
# x = iter(['apple', 'banana', 'cherry'])
# print(next(x))
# print(next(x))
# print(next(x))

# ------------------------------------------------------------------------------
# len()          Returns the length of an object
# ------------------------------------------------------------------------------
# list()      Returns a list
# ------------------------------------------------------------------------------
# next()      Returns the next item in an iterable
#           RU: Возвращает следующий элемент в итерируемом объекте
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
# ------------------------------------------------------------------------------
# oct()          Converts a number into an octal
#           RU: Преобразует число в восьмеричное число
#           EX:
#               x = oct(8)   =>  0o10
#               z = oct(18)  =>  0o22
# ------------------------------------------------------------------------------
# open()      Opens a file and returns a file object
# ------------------------------------------------------------------------------
# ord()       Convert an integer representing the Unicode of the specified character
#           RU: Преобразовать целое число, представляющее Юникод указанного символа
#           EX:
# x = ord('a')  # =>  97
# print(x)
# x = ord('A')  # =>  65
# print(x)



# ------------------------------------------------------------------------------
# pow()          Returns the value of x to the power of y
# print(pow(3, 5)) #  =>  243
# ------------------------------------------------------------------------------
# print()      Prints to the standard output device
# ------------------------------------------------------------------------------
# property  Gets, sets, deletes a property
#           RU: Получает, устанавливает, удаляет свойство
#           EX:
#               class Person:
#                   def __init__(self, name, age):
#                       self.name = name
#                       self.age = age
#
#                   @property
#                   def fullName(self):
#                       return self.name + ' ' + self.age
# ------------------------------------------------------------------------------
# range()      Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# ------------------------------------------------------------------------------
# repr()      Returns a readable version of an object
#           RU: Возвращает читаемую версию объекта
#           More info:
#           https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/repr/python-repr/#:~:text=a%20Python%20repr%3F-,The%20Python%20repr()%20method%20is%20mostly%20used%20for%20the,specified%20object%20as%20a%20string.
#
#           EX:
#               x = repr('Hello')
#               print(x)  =>  'Hello'
# ------------------------------------------------------------------------------
# reversed()  Returns a reversed iterator
#           RU: Возвращает обратный итератор
#           EX:
#               x = reversed(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  cherry
# x = [1, 2, 3]
# z = list(reversed(x))
# print(z)
# print(x)
# x.reverse()
# ------------------------------------------------------------------------------
# round()      Rounds a numbers
#           RU: Округляет числа
#           EX:
# x = round(5.16543, 2)
# print(x) # =>  5.17
# x = 5.76543
# print(round(x, 2))
# ------------------------------------------------------------------------------
# set()          Returns a new set object
# ------------------------------------------------------------------------------
# setattr()      Sets an attribute (property/method) of an object
#           RU: Устанавливает атрибут (свойство / метод) объекта
#           EX:
#               class Person:
#                   name = 'John'
#                   age = 36
#               x = setattr(Person, 'age', 40)
# ------------------------------------------------------------------------------
# slice()      Returns a slice object
#           RU: Возвращает объект среза
#           EX:
# x = slice(1, 3)
# fruits = ['apple', 'banana', 'cherry', 'orange']
# print(fruits[x])  # =>  ['apple', 'banana', 'cherry']
# ------------------------------------------------------------------------------
# sorted()      Returns a sorted list
#           RU: Возвращает отсортированный список
#           EX:
#               x = sorted(['apple', 'banana', 'cherry', 'orange'])
# ------------------------------------------------------------------------------
# staticmethod()  Converts a method into a static method
# ------------------------------------------------------------------------------
# str()          Returns a string object
# ------------------------------------------------------------------------------
# sum()          Sums the items of an iterator
# ------------------------------------------------------------------------------
# super()      Returns an object that represents the parent class
# ------------------------------------------------------------------------------
# tuple()      Returns a tuple
# ------------------------------------------------------------------------------
# type()      Returns the type of an object
# ------------------------------------------------------------------------------
# vars()      Returns the __dict__ property of an object


#           RU: Возвращает свойство __dict__ объекта
#           EX:
# class Person:
#     name = 'John'
#     age = 36

# x = vars(Person)
# print(list(x)) #  =>  {'name': 'John', 'age': 36}
# ------------------------------------------------------------------------------
# zip()          Returns an iterator, from two or more iterators
#           RU: Возвращает итератор из двух или более итераторов
#           EX:
# x = zip(['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple'])
# print(next(x))  # =>  ('apple', 'orange') 
# ------------------------------------------------------------------------------


#! for more info visit sites:
#* 1. Programmiz  =  https://www.programiz.com/python-programming/methods/built-in
#* 2. w3schools   =  https://www.w3schools.com/python/python_ref_functions.asp
#* 3. python.org  =  https://docs.python.org/3/library/functions.html