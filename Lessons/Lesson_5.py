# def show_message(arg):
#     print('Hello world')


#...rest => JS
# *rest  => Python

# def sum_number(*number:int): 
#     result = 0
#     for num in number:
#         result += num
#     print(result)    

# sum_number(12, 12, 12, 12)

# def factorial(num:int) -> int:
#     print(num)
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# # 5 * 4 * 3 * 2 * 1  ==>  факториал 5   ==  !5   ==  120
# summa = factorial(5)
# print(summa)

# def show_start(num:int) -> None:
#     star = '*'
#     if num == 1:
#         print(star)
#     else:
#         print(star * num)
#         show_start(num-1)

# show_start(10)

# pass
# def show_message(*children):
#     """This function needs to be finished in near future!"""
#     # return NotImplementedError()  =>  не было создано!
#     pass

#! ----------------------------------------------------------

# def func_name(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
# func_name(1, 2, 3)
#! ----------------------------------------------------------
# from typing import Union
# def func_name(arg1:Union[str, int]) -> type:
#     return arg1
# print(func_name(1))


# def show_message(number:int) -> str:
#     if true_or_false := even_odd(number):
#         print (f"{number} is Even")
#         print (true_or_false)
#     else:
#         print (f"{number} is Odd")
# show_message()
#! ----------------------------------------------------------

# default value
# def blender(fruits:Union[str, list]='Apple') -> None:
#     if type(fruits) == list:
#         for fruit in fruits:
#             print(f"{fruit} juice is ready!")
#     else:
#         fruit = fruits
#         print(f"{fruits} juice is ready!")

# blender(["Apple", "Orange", "Banana"])

#! ----------------------------------------------------------
# Lambda
# func_name = lambda arg1, arg2: arg1 + arg2
# print(func_name(1, 2))
#! ----------------------------------------------------------
# RECURSION
# def factorial(num:int) -> int:
#     print(num)
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# # 5 * 4 * 3 * 2 * 1  ==>  факториал 5   ==  !5   ==  120
# summa = factorial(5)
# print(summa)