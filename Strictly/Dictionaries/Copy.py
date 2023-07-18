
#! You cannot copy a dictionary simply by typing dict2 = dict1, 
#! because: dict2 will only be a reference to dict1, and changes 
#! made in dict1 will automatically also be made in dict2.

#? Have a two methos

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
