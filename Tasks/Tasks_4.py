def multiply_list(arr):
    result = 1
    for i in arr:
        result *= i
    return result

def smalilest_greatest_sum(arr):
    smallest = arr[0]
    greatest = arr[0]
    for number in arr:
        if greatest < number:
            greatest = number
        if smallest > number:
            smallest = number
    x = greatest + smallest
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
    return x

def count_strings(arr):
    counter = []
    for items in arr:
        first_two = items[0:2]
        if first_two[::-1] == items[-2:]:
            counter.append(items)
    return counter

def sort_tuple(tup: tuple) -> tuple:
    even = []
    odd = []
    for items in tup: 
        if items % 2 == 0:
            even.append(items)
        else:
            odd.append(items)
    even.sort(reverse=True)
    odd.sort(reversed=True) 
    return tuple(even + odd)

def remove_key(dc, _key):
    dict_copy = dc.copy()
    dict_copy.pop(_key)
    return dict_copy

def remove_duplicates(dict):
    for key, val in dict.items():
        if dict.values().count() > 1:
            del dict[key]
    return dict

def get_keys_greater_than(dict, num):
    result = {}
    for key, val in dict.items():
        if str(val).isnumeric():
            if val > num:
                result[key] = val
    return result

def reverse_dict(d):
    return {val: key for key,val in d.items()}

def sum_numeric_values(arr_of_dicts: list[dict]) -> int:
    total = 0
    for dic in arr_of_dicts:
        for v in dic.values():
            if str(v).isnumeric():
                total += int(v)
    return total

x = {'a': 1, 'b': "2", "c": "Hello"}
z = {'d': "4", 'e': 3, "f": "World"}
a = {'g': 5, 'h': "!!!", "i": "6"}
arr = [x, z, a]

print(sum_numeric_values(arr))