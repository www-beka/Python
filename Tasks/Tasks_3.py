# 3. Write a program that takes a list of strings as input and returns the longest string.
# RU: Напишите программу, которая принимает список строк в качестве входных
# данных и возвращает самую длинную строку.
def longest_word(arr):
    return max(arr, key=len)


# 4. Write a program that takes a string as input and returns the number of letters in each string.
# RU: Напишите программу, которая принимает строк в качестве входных данных
# и возвращает количество букв в каждой строке.
def letters_in_string(string):
    x = list(string)
    print(len(x))


# 5. Write a program that takes a list of numbers as input and
# returns the average of the numbers.
# RU: Напишите программу, которая принимает список чисел в качестве
# входных данных и возвращает среднее значение чисел.
# [13, 22, 35, 41, 52]   => 13+22+35+41+52 = 163 / 5 = 32.6

from functools import reduce

def average_of_numbers(arr):
    summ = reduce(lambda acc, next: acc + next, arr)
    round_number = round(summ / len(arr), 2)
    x = min(arr, key=lambda x: abs(x-round_number))
    print(x)

numbers = [13, 22, 35, 41, 52]

average_of_numbers(numbers)
