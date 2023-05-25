## 1. Write a function to swap the first and last characters in a string.
# RU: Напишите функцию, чтобы поменять местами первый и последний символы в строке.
def swap_first_last(string):   # поменять_первый_последный
    return string[-1] + string[1:-1] + string[0]


## 2. Write a function to reverse a string.
# RU: Напишите функцию, чтобы перевернуть строку.
def reverse_string(string): # перевернуть_строку
    return string[::-1]


## 3. Write a function to remove the nth index character from a n onempty string.
# RU: Напишите функцию, чтобы удалить символ с индексом n из непустой строки.
def remove_nth_index(string, index): # удалить_с_индексом
    return string[:index] + string[index+1:]



## 4. Write a function to remove the characters which have odd index values of a given string.
# RU: Напишите функцию, чтобы удалить символы, которые имеют нечетные индексы заданной строки.
def remove_odd_index(string): # удалить_нечетные_индексы
    return string[::2] 


## 5. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# RU: Напишите скрипт Python, который принимает ввод от пользователя и отображает этот ввод в верхнем и нижнем регистрах.
def upper_lower(string): # верхний_нижний
    return string.upper(), string.lower()



## 6. Write a function to find the second most frequent character in a given string.
# RU: Напишите функцию, чтобы найти второй наиболее часто встречающийся символ в данной строке.
def second_most_frequent(string): # второй_наиболее_часто_встречающийся
    dict = {}
    for i in string:
        dict[i] = string.count(i)
    return sorted(dict.items(), key=lambda x: x[1])[-2][0]


## 7. Write a function to convert a given string into a list of integers.
# RU: Напишите функцию, чтобы преобразовать заданную строку в список целых чисел.
def convert_to_list(string): # преобразовать_в_список
    return [int(i) for i in string]


## 8. Write a function to check if a given string is a palindrome.
# RU: Напишите функцию, чтобы проверить, является ли заданная строка палиндромом.
def is_palindrome(string): # является_палиндромом
    return string == string[::-1]


## 9. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
# RU: Напишите программу на Python, чтобы получить строку, состоящую из первых 2 и последних 2 символов заданной строки.
# Если длина строки меньше 2, вместо этого верните пустую строку.
def first_last_two(string): # первые_2_последние_2
    if len(string) < 2:
        return ''
    return string[:2] + string[-2:]


# #10. Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$', except the first char itself.
# RU: Напишите программу на Python, чтобы получить строку из заданной строки, где все вхождения ее первого символа
# были заменены на '$', кроме самого первого символа.
def change_first_char(string:str, symbol:str="$") -> str: # изменить_первый_символ
    first = string[0]
    rest = string[1:].lower()
    return first + rest.replace(first.lower(), symbol)

print(change_first_char("Zamzam Azam zam"))
print(change_first_char("Aziz ziz aziz ziz ziz Aaziz", "^"))


# #11. Write a Python program to get a single string from two given strings, separated by a space and 
# swap the first two characters of each string.
# RU: Напишите программу на Python, чтобы получить одну строку из двух заданных строк, разделенных пробелом и
# поменять местами первые два символа каждой строки.
def swap_first_two(string1, string2): # поменять_первые_два
    return string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]



# #12. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string 
# already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# RU: Напишите программу на Python, чтобы добавить 'ing' в конец заданной строки (длина должна быть не менее 3).
# Если заданная строка уже заканчивается на 'ing', вместо этого добавьте 'ly'. 
# Если длина строки заданной строки меньше 3, оставьте ее без изменений.
def add_ing(string): # добавить_ing
    if len(string) < 3:
        return string
    if string[-3:] == 'ing':
        return string + 'ly'
    return string + 'ing'


# #13. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# RU: Напишите программу на Python, чтобы найти первое появление подстрок «не» и «плохо» в заданной строке.
# Если «не» следует за «плохо», замените всю подстроку «не» ... «плохо» на «хорошо». Вернуть полученную строку.
def replace_not_poor(string): # заменить_не_плохо
    not_index = string.find('not')
    poor_index = string.find('poor')
    if not_index != -1 and poor_index != -1 and poor_index > not_index:
        return string.replace(string[not_index:poor_index+4], 'good')
    else:
        return string


# #14. Write a Python function to create an HTML string with tags around the word(s)
# RU: Напишите функцию Python для создания HTML-строки с тегами вокруг слова (слов).
def add_tags(tag, string): # добавить_теги
    return f'<{tag}>{string}</{tag}>'


# #15. Write a Python function to insert a string in the middle of a string.
# RU: Напишите функцию Python для вставки строки посередине строки.
def insert_string_middle(string, string_to_insert): # вставить_строку_посередине
    return string[:len(string)//2] + string_to_insert + string[len(string)//2:]


# #16. Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# RU: Напишите функцию Python, чтобы получить строку, состоящую из 4 копий последних двух символов заданной строки
def last_two(string): # последние_два
    return string[-2:] * 4


# #17. Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.
# RU: Напишите функцию Python, чтобы получить строку, состоящую из первых трех символов заданной строки.
# Если длина строки меньше 3, вернуть исходную строку.
def first_three(string): # первые_три
    if len(string) < 3:
        return string
    return string[:3]


# #18. Write a Python function to get the first half of a specified string of even length.
# RU: Напишите функцию Python, чтобы получить первую половину заданной строки четной длины.
def first_half_even(string): # первая_половина_четная
    if len(string) % 2 == 0:
        return string[:len(string)//2]
    return string

# #19. Write a Python program to concatenate two strings and return the result. 
# If the length of the strings are not same then remove the characters from the longer string.
# RU: Напишите программу на Python для объединения двух строк и верните результат. Если длины строк не одинаковы,
# то удалите символы из более длинной строки.
def concat_strings(string1, string2): # объединить_строки
    if len(string1) == len(string2):
        return string1 + string2
    elif len(string1) > len(string2):
        return string1[:len(string2)] + string2
    else:
        return string1 + string2[:len(string1)]
    


# #20. Write a Python function to convert a given string to all uppercase if it contains 
# at least 2 uppercase characters in the first 4 characters.
# RU: Напишите функцию Python для преобразования заданной строки в верхний регистр, если она содержит
# не менее 2 заглавных символов в первых 4 символах.
def convert_upper(string): # преобразовать_в_верхний_регистр
    if sum(1 for char in string[:4] if char.isupper()) >= 2:
        return string.upper()
    return string


# #21. Write a Python program to remove a newline in Python.
# RU: Напишите программу на Python, чтобы удалить перевод строки в Python.
def remove_newline(string): # удалить_перевод_строки
    return string.replace('\n', '')


# #22. Write a Python program to remove existing indentation from all of the lines in a given text.
# RU: Напишите программу на Python для удаления существующего отступа из всех строк в заданном тексте.
def remove_indentation(string): # удалить_отступ
    return string.strip()


# #23. Write a Python program to count and display the vowels of a given text.
# RU: Напишите программу Python, чтобы подсчитать и отобразить гласные заданного текста.
def count_vowels(string): # подсчитать_гласные
    vowels = 'aeiou'
    return sum(1 for char in string if char in vowels)



# def swap_cases(string): # поменять_регистр
#     return string.swapcase()