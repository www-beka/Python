
#! Выведите второй элемент кортежа:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#! Выведите последний элемент кортежа:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#! Вернуть третий, четвертый и пятый элемент:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

## Поиск начнется с индекса 2 (включительно) и закончится с индексом 5 (не включено).
#? Помните, что первый элемент имеет индекс 0.

#! В этом примере возвращаются элементы с самого начала, но НЕ включенные в "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#! Этот пример возвращает элементы от "cherry" и до конца:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#! В этом примере возвращаются элементы из индекса -4 (включено) в индекс -1 (исключено)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#! Проверьте, присутствует ли «apple» в кортеже:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")