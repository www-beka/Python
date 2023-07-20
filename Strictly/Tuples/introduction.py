
#! What is Tuple
##   Tuple
#?     Tuple используются для хранения нескольких элементов в одной переменной.
#?     Tuple — это один из 4 встроенных типов данных в Python, 
#?     используемых для хранения коллекций данных, остальные 3 — List , Set и Dictionary , 
#?     все с разными качествами и использованием.
#?     Tuple — это упорядоченная и неизменяемая коллекция .
#?     Tuple пишутся с круглыми скобками.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#! Чтобы создать кортеж только с одним элементом, 
#!    вы должны добавить запятую после элемента, 
#!       иначе Python не распознает его как кортеж.

thistuple = ("apple",)
print(type(thistuple))

#!NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#! Также можно использовать конструктор tuple() для создания кортежа.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
