# SETS
# sequence in russian is последовательность

# -----------------------------------------------------------------------------------
# CREATE --------------------------------------------------------------------
# Use curly braces or the built-in set function.

# my_set = {"apple", "banana", "cherry"}
# print(my_set)

# # or use the set function and create from an iterable, e.g. list, tuple, string
# my_set_2 = set(["one", "two", "three", "three"])
# my_set_2 = set(("one", "two", "three"))
# print(my_set_2)

# my_set_3 = set("aaabbbcccdddeeeeeffff")
# print(my_set_3)

# # careful: an empty set cannot be created with {}, 
# # as this is interpreted as dict
# # use set() instead
# a = {}
# print(type(a))
# a = set()
# print(type(a))
# {'banana', 'apple', 'cherry'}
# {'three', 'one', 'two'}
# {'b', 'c', 'd', 'e', 'f', 'a'}
# <class 'dict'>
# <class 'set'>


# -----------------------------------------------------------------------------------
# NOTES  -----------------------------------------------------
# test_set = {1, 2, 3, 4, 5}
# Does not allow duplications
# Does not have order, index, keys, values, items, slices, etc...

# 1 and True are the same and 0 and False are the same
# 1 == True  =>  True
# 0 == False  =>  True
# 1 is True  =>  False
# 0 is False  =>  False

# -----------------------------------------------------------------------------------
# ACCESSING ITEMS --------------------------------------------
# loop   ||    ... in ...
# EX: 
# x = {1, 2, 3, 4, 5}
# for i in x:
#     if 2 == i:
#         print(i)
#     else:
#         print("Not 2")

# -----------------------------------------------------------------------------------
# ADDING -----------------------------------------------------
# Добавлять

# add()                  Adds an element to the set
#   EX: x.add(4)  => changes the original set

# x = {1, 2, 3}
# x.add(3) # Does not add duplicate
# x.add(4) # Adds
# print(x)

# update()  =>   Updates the set with the union of this set and others
# RU:            Обновит оригинальный. Только добавит тех которых не имеет 
#  EX: x.update([4, 5, 6])  => changes the original set

# x.update([4, 5, 6])
# print(x)

# -----------------------------------------------------------------------------------
# # Union and Intersection

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
# u = odds.union(evens)
# print(u)
# EX: 
# a = x.union(y)  =>  x | y
# u = odds | evens
# print(u)

# intersection(): take elements that are in both sets
# return a new set, that only contains the items that are present in both sets.
# Берёт только дупликатов
# i = odds.intersection(evens)
# print(i)
# # EX: x.intersection(y)  =>  x & y
# i = odds & evens
# print(i)

# -------------------
# x = {1, 3, 3, 2, 5}
# z = {1, 5, 7, 8}
# i = x.intersection(z)
# print(i)
# -------------------
# i = evens.intersection(primes)
# print(i)

# -----------------------------------------------------------------------------------
# # DIFFERENCE of sets
# setA = {4, 6,  5, 1, 2, 3 }
# setB = {1, 2, 3, 10, 11, 12}
# setC = {1, 2, 3, 15, 16}

# # difference() : returns a set with all the elements from the setA that are not in setB or in B,C,... .
# # x.difference(y)     =>  x - y
# # x.difference(y, z)  =>  x - y - z
# diff_set_A = setA.difference(setB)
# print(diff_set_A)
# diff_set_B = setB.difference(setA)
# print(diff_set_B)
# diff_set_A = setA.diffe   rence(setB, setC)
# print(diff_set_A)

# # A.difference(B) is not the same as B.difference(A)
# diff_set = setB.difference(setA)
# print(diff_set)

# # symmetric_difference() : 
# returns a set with all the elements that are in setA and setB but not in both
# diff_set = setA.symmetric_difference(setB)
# print(diff_set)

# # A.symmetric_difference(B) = B.symmetric_difference(A)
# diff_set = setB.symmetric_difference(setA)
# print(diff_set)



# -----------------------------------------------------------------------------------
# DELETE