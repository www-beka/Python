thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(thisdict[x])
#! Print all values in the dictionary, one by one:

for x in thisdict.values():
  print(x)

#! You can also use the values() method to return values of a dictionary:

for x in thisdict.keys():
  print(x)

#! You can use the keys() method to return the keys of a dictionary:

for x, y in thisdict.items():
  print(x, y) ## x => key of "dict", y => values of "dict"

#! Loop through both keys and values, by using the items() method: