# def sort_tuple(tup):
#     even = []
#     odd = []
#     for i in tup:
#         if i % 2 == 0:
#            even.append(i)
#         else:
#             odd.append(i)
#     result = (*sorted(even)[::-1], *sorted(odd)[::-1]) 
    
#     return result


# x = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# print(sort_tuple(x))


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict

# print(char_frequency('google.com'))


# def chnage_first(string:str, symbol:str="$") -> str: # изменить_первый_символ
#     x = string[0]
#     y = string[1:].lower()
#     return x + y.replace(x.lower(), symbol)

# x = [1, 4, 11, 114, 12, 24, 55]
# targets = 23

# def find_target(arr, target):
#     for item1 in arr:
#         for item2 in arr:
#             item1_index = arr.index(item1)
#             item2_index = arr.index(item2)
#             sum = item1 + item2
#             if item1 != item2 and item1_index != item2_index and sum == target:
#                 print(item1_index, item2_index)
#                 return


# find_target(x, targets)


dict = {
    'a': 1, 'b': 2,  
}
