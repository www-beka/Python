# def concatenate_dictionaries(*args):
    # dict = {}
    # for i in args:
    #     dict.update(i)
    # return dict
    # return {key: value for dicts in args for key, value in dicts.items()}

# x2 = {"c": 3, "d": 4}
# x3 = {"e": 5, "f": 5}
# x4 = {"g": 6, "h": 5}


# def check_key(dict, key):
#     return key in dict



# def interate_over_dict(dict):
#     for k,v in dict.items():
#         print(k,v)
#     return {"":print(k,v) for k,v in dict.items()}


def sum_dict(dict):
    total = 0
    # for i in dict.values():
    #     if type(i) == int:
    #         total += i
    #     elif i.isnumeric():
    #         total += int(i)
    # return total
    # return {if type(val) == int: total += val for val in dict.values(): }
x = {"a": 1, "b": "2"} 
print(sum_dict(x))

