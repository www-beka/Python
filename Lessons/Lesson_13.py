# numbers = [22, 13, 5, 9, 10,  14, 33]
# # z =     [2,   3, 0, 4,  0,  4,   3]

# x = max(numbers, key=lambda num: num % 5)
# print(x)

# 11 / 2 = 5.5
# 11 % 2 = 1

# max()        
# Return the largest item in an iterable or the largest of two or more arguments.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.

# If one item is given, it should be iterable. The largest item in the iterable is returned.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.
# max(iterable, *[, key, default])

# If two or more positional arguments are provided, the largest of the positional arguments is returned.
# RU: Если предоставлено два или более позиционных аргумента, возвращается наибольший из позиционных аргументов.
# max(arg1, arg2, *args[, key])

# There are two optional keyword-only arguments.
# RU: Есть два необязательных аргумента только ключевых слов.

# key- key function where the iterables are passed and comparison is performed based on its return value
# RU: key- ключевая функция, в которой передаются итерируемые объекты, 
# и сравнение выполняется на основе возвращаемого значения
# EX: 
#   iterable = ['geeks', 'code', 'python', 'java']
#   max(iterable, key=len)  =>  'python'
# iterable = [30, 15, 20, 25, 30]
# print(max(iterable, key=lambda x: x%15))  # => 25 
#   => here the remainder after dividing each element by 
#      15 is calculated and the maximum of those values is returned
#      ex:  10%15 = 10,  15%15 = 0,  20%15 = 5,  25%15 = 10,  30%15 = 0 

# The default argument specifies an object to return if the provided iterable is empty. 
# If the iterable is empty and the default is not provided, a ValueErroris raised.
# EX: 
#   iterable = []
#   max(iterable, default=100)  =>  100
#   max(iterable)  =>  ValueError: max() arg is an empty sequence
# ==================================
# min()         Works the same way as max(), but returns the smallest value
#           RU: Работает так же, как max (), но возвращает наименьшее значение


# ===========================================================================================
# map()         Returns a map object (which is an iterator) of the results after applying the 
#               given function to each item of a given iterable (list, tuple etc.)
#           RU: Возвращает объект отображения (который является итератором) результатов после применения
#               заданной функции к каждому элементу заданного итерируемого объекта (список, кортеж и т. Д.)
#           EX:
#               def wordCount(n):
#                   return len(n)
#               x = map(wordCount, ('apple', 'banana', 'cherry'))
#               print(list(x))  => [5, 6, 6]

# x = ["apple", "banana", "cherry"]
# y = map(len, x)
# print(list(y))
# ==================================
# let y = x.map(num => String(num).length)  #  in JS


# ------------------------------------------------------------------------------
# filter()      Use a filter function to exclude items in an iterable object
#           RU: Используйте функцию фильтра, чтобы исключить элементы в итерируемом объекте
#           EX:
def myFunc(n):
    if n > 18:
        return True
    else:
        return False
    # -------------------
    # return True if n > 18 else False
    # -------------------
    # return n > 18
    # -------------------
    # lambda x: x>18
#               x = filter(myFunc, (5, 7, 18, 25, 32))
#               print(list(x))  =>  [25, 32]
# test_tuple = (5, 7, 18, 25, 32)
# test_tuple = filter(myFunc, test_tuple)
# print(list(test_tuple))
# =========================================
# let y = x.filter(num => num > 18)  #  in JS



# ------------------------------------------------------------------------------
# reduce()      Use a function to reduce an iterable to a single value
#           RU: Используйте функцию для сокращения итерируемого объекта до одного значения
#           EX:
from functools import reduce
def myFunc(acc, next):
    """
        acc  - accumulator  => миксер или смеситель
        next - next value   => следующее значение
        NOTE: the initial value of the accumulator is the first value of the iterable
    """
    return acc + next

    
x = reduce(myFunc, (1, 2, 3, 4))
# 1 + 2
# 3 + 3
# 6 + 4
print(x)  # =>  10