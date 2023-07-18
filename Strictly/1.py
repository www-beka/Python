
# del variable	 =>   удаление переменной
# del obj.attr	 =>   удаление атрибута
# del data[k]	 =>   удаление элемента по индексу
# del data[i:j]	 =>   удаление элементов по срезу


# print("Studytonight", end= "\n") => "end" default new line
# print("Study", "tonight", sep = ' & ')  => "sep" take anything 

# def anything(*par):    | => default function    
#     return sum(par)    | => default function    
# print(anything(12, 12))| => default function        

# x = lambda *par : sum(par)| => "lambda" function
# print(x(12, 12))          | => "lambda" function

x = ('some', 1, False)
c = tuple(('some', 1, False))

print(type(x))
print(type(c))

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


# tuple poxosh na const iz JS ne menayetsa   
