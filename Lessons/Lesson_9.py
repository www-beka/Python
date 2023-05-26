SeventhLesson = "Dictionaries  =>  словарь"
# x = {"first": "Один", "second": "Два",
#     "third": "Три", "fourth": "Четыре",
#     "fifth": "Пять", "sixth": "Шесть",
#     "seventh": "Семь", "eighth": "Восемь",
# }
# print(x.get("fourth", "Не нашлось"))
# ------------------------------------------------
# z = [ "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь" ]
# for i in z:
#     if i == "Четыре":
#         print(i)
# ------------------------------------------------

# dict()  =>  dict(key=value, key=value, key=value)

# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}



# # ACCESSING ITEMS ---------------------------------------------------------------------------

# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default
# dict.keys()       => возвращает список ключей
# dict.values()     => возвращает список значений
# dict.items()      => возвращает список кортежей (ключ, значение)

# # ADDING ITEMS -----------------------------------------------------------------------------
# dict[key] = value
# -----------------
# dict.update({key:value, key:value, key:value})
# person.update({"name": "Alex", "address": "Samarkand"})
# -----------------
# dict.setdefault(key, value)
# person.setdefault("address", "Tashkent")


# # REMOVING ITEMS ---------------------------------------------------------------------------

# dict.pop(key)
# dict.pop(key, default)
# dict.popitem() => removes the last inserted item
# del dict[key]
# del dict

# # MERGE ------------------------------------------------------------------------------------
# dict1.update(dict2)
# dict1 |= dict2
# dict1 |= dict2 | dict3 | dict4
# {**dict1, **dict2, **dict3, **dict4}

# person2 = { "name2":"John",  "age2":20,  "surname2":"Khan",  "address2":"Samarkand" }
# person3 = {1:'a', 2:'b'}
# -----------------------------------
# person |= person2 | person3 
# -----------------------------------
# a = {**person, **person2, **person3 } 
# works like spread operator in JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# dict.clear()
# dict.copy()

# for key in person.keys():
#     person[key] = ""

# p2 = person.copy()
# p2.update({"name":"Ali"})
# print(p2)
# print(person)

# person = {
#     "name": "John",
#     "age": 20,
#     "surname": "Khan",
#     "address": "Samarkand"
# }

# dict.fromkeys(iterable, value)  -> is used to create a new dictionary from the given 
#                                    sequence of elements with a value provided by the user.
# EX: 
# x = dict.fromkeys(['name', 'age'], 'unknown')
# print(x)
# 1. Write a Python function that takes a list of words and returns the length of the longest one.
# RU: Напишите функцию Python, которая принимает список слов и возвращает длину самого длинного слова.
x = ['qweqwe', 'wwwwwwwwwwwwwwwwww', 'qqqqqqqqq', 'eee']
def longest_word(arr):
    a = arr[0]
    for word in arr:
        if len(word) > len(a):
            a = word
    return arr.index(a)
print(longest_word(x)) # 1