
## После создания tuple вы не можете изменить его значения. tupleи неизменяемы , 
## или неизменны, как это еще называется.

## Но есть обходной путь. Вы можете преобразовать tuple в list,
## изменить list и снова преобразовать list в tuple. 

#! Преобразуйте tuple в list, чтобы иметь возможность его изменить:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

## Поскольку tuple неизменяемы, у них нет встроенного append() метода,
## но есть и другие способы добавления элементов в tuple.

## Преобразование в list . Как и обходной путь для изменения tuple,
## вы можете преобразовать его в list, добавить свои элементы и снова преобразовать его в tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

## Вам разрешено добавлять tuple в tuple, поэтому, если вы хотите добавить один элемент (или несколько), 
## создайте новый tuple с элементами и добавьте его в существующий tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y  #!

print(thistuple)

#! remove

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#! Чтобы объединить два или более кортежа, вы можете использовать + оператор:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)