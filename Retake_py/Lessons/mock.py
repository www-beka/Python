# def insert_string_middle(string, string_to_insert):
#     return string[:len(string) // 2] + string_to_insert + string[len(string) // 2:]

# def first_three(string):
#     return string[0:3]

# def first_half_even(string):
#     if len(string) % 2 == 0:
#         return string[:len(string) // 2]
#     return string

# print(first_half_even('Bekzod'))

# def concant_string(string1, string2):
#     return str(string1) + str(string2)


# def remove_indentation(string):
#     return str(string).replace(' ', '')

# def count_vowels(string):
#     v = 'aeiou'
#     counter = 0
    
#     for i in string:
#         i = i.lower()
#         if i in v:
#             counter = counter+1
#     return counter     

# def swap_case(string):
#     return str(string).swapcase()

# def chek_dublcate_letters(string) -> bool:
#     for letter in string:
#         index_of_letter = string.index(letter)
#         if string[index_of_letter-1] == letter or string[index_of_letter+1]:
#             return True
#     return False



# def piramid(star):
#     if star == 1:
#         return "*"
#     else:
#         return "*" * star,'\n' + piramid(star-1)

# print(piramid(10))

# def show_stars(num:int):
#     stars = '*'
#     if num == 1:
#         print(stars)
#     else:
#         show_stars(num-1)
#         print(stars * num)


# show_stars(10)


# 7.  Write a Python program to count the number of strings from a given
# list of strings. The string length is 2 or more and the first
# and last characters are the same.
# RU: Напишите программу Python, чтобы подсчитать количество строк из заданного
# список строк. Длина строки 2 или более, а первые 2 и последние 2 символы одинаковы.
# ['abc', 'xyz', 'aba', '1212381923128321']
# Expected Result : 2


def count_strings(arr):
    pass

# 8. Write a Python program to remove duplicates from a list.
# RU: Напишите программу Python, чтобы удалить дубликаты из списка.


def remove_duplicates(arr:list):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicates([1, 1, 2, 3]))

# 14. Create a function that takes a list of names and returns the
# ones that start with a vowel.
# RU: Создайте функцию, которая принимает список имен и возвращает те,
# которые начинаются с гласной буквы.


def get_names_starting_with_vowel(arr:list):
    vowels = 'aeiou'
    result = []
    for letter in arr:
        if letter[0].lower() in vowels:
            result.append(letter)
    
    print(result)

    


get_names_starting_with_vowel(['Alex', 'Max', 'Elizaphat'])