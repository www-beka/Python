
#! Метод union() возвращает новый набор со всеми элементами из обоих наборов:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#! Метод update() вставляет элементы из set2 в set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#! Метод intersection_update() сохранит только те элементы, которые присутствуют в обоих наборах.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

#! Метод intersection() вернет новый набор, содержащий только те элементы, которые присутствуют в обоих наборах.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

#! Метод symmetric_difference_update() сохранит только те элементы, которые НЕ присутствуют в обоих наборах.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

#! Метод symmetric_difference() вернет новый набор, содержащий только те элементы, которые НЕ присутствуют в обоих наборах.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)