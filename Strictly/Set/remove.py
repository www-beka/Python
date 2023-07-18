
#! SET Loop ===========
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#! =======================

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #! Just remove😂

#! If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #! Just remove😂

#! If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() #! remove random element

thisset = {"apple", "banana", "cherry"}

thisset.clear() #! The clear() method empties the set:😅

thisset = {"apple", "banana", "cherry"}

del thisset #! delet all elments
