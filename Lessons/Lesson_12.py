

# remove(x): removes x, raises a KeyError if element is not present
# my_set = {"apple", "banana", "cherry"}
# my_set.remove("apple")
# print(my_set)

# # KeyError:
# # my_set.remove("orange")

# # discard(x): removes x, does nothing if element is not present
# my_set.discard("cherry")
# my_set.discard("blueberry")
# print(my_set)

# # clear() : remove all elements
# my_set.clear()
# print(my_set)

# # pop() : return and remove a random element
# a = {True, 2, False, "hi", "hello"}
# x = a.pop()
# print(a)
# print(x)

# -----------------------------------------------------------------------------------
# Check if element is in Set
# my_set = {"apple", "banana", "cherry"}
# if "apple" in my_set:
#     print("yes")


# -----------------------------------------------------------------------------------
# # UPDATE sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# # update() : Update the set by adding elements from another set.
# setA.update(setB)
# print(setA)

# # Keep ONLY the Duplicates
# # intersection_update() : 
# # Update the set by keeping only the elements found in both
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.intersection_update(setB)
# print(setA)

# # difference_update() : 
# # Update the set by removing elements found in another set.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.difference_update(setB)
# print(setA)

# # symmetric_difference_update():  
# # Keeps only the elements that are NOT present in both sets.
# # Keep All, But NOT the Duplicates. 
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.symmetric_difference_update(setB)
# print(setA)

# # Note: all update methods also work with other iterables as argument, 
# e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])

# -----------------------------------------------------------------------------------
# Copying ---------------------------------------------------------------------------
# set_org = {1, 2, 3, 4, 5}

# # this just copies the reference to the set, so be careful
# set_copy = set_org

# # now modifying the copy also affects the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)

# # use copy() to actually copy the set
# set_org = {1, 2, 3, 4, 5}
# set_copy = set_org.copy()

# # # now modifying the copy does not affect the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)

# -----------------------------------------------------------------------------------
# Subset, Superset, and Disjoint ----------------------------------------------------
# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
# print(setA.issubset(setB))
# print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
# print(setA.issuperset(setB)) # True
# print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, 
# i.e. no same elements
# setC = {7, 8, 9}
# print(setA.isdisjoint(setB)) # False
# print(setA.isdisjoint(setC)) # True
# -----------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# FROZENSET
# # Frozen set is just an immutable version of normal set. 
# # While elements of a set can be modified at any time, elements of frozen set 
# # remains the same after creation. 
# # Creation with: my_frozenset = frozenset(iterable)

# a = frozenset([0, 1, 2, 3, 4])

# # The following is not allowed:
# # a.add(5)
# # a.remove(1)
# # a.discard(1)
# # a.clear()

# # Also no update methods are allowed:
# # a.update([1,2,3])

# Other set operations work
# odds = frozenset({1, 3, 5, 7, 9})
# evens = frozenset({0, 2, 4, 6, 8})
# print(odds.union(evens))
# print(odds.intersection(evens))
# print(odds.difference(evens))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# frozenset()
# frozenset({1, 3, 5, 7, 9})
# ------------------------------------------------------------------------------------