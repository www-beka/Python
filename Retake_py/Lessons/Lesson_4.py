from functools import reduce

def sum_and_compare(arr):
    summ = reduce(lambda acc, next: acc + next, arr)
    maximun = max(arr)
    result = summ - maximun

    print(f'{result} Even' if result % 2 == 0 else f'{result} Odd')


# print(sum_and_compare(numbers))



def third_biggest(arr:list):
    copy_l = arr.copy()
    biggest = max(copy_l)
    copy_l.remove(biggest)
    bigges_2 = max(copy_l)
    copy_l.remove(bigges_2)
    return max(copy_l)


numbers = [1,2,3,4,5,6,7,8,9]
print(third_biggest(numbers))