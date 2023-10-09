# -----------------------------------
# `${......}` => String template  => JS
#  f{......}  => f string         => Python
# -----------------------------------
# a, b, c = [1, 2, 3]
# print(a, b, c, sep="-")



# num_1 = int(input('Enter first number:'))
# num_2 = int(input('Enter second number:'))
# plus_or_minus = input('Enter symbol:')

# if plus_or_minus == '+':
#     print("The sum of two numbers is", num_1 + num_2)
# elif plus_or_minus == '-':
#     print("The difference between the two numbers is ", num_1 - num_2)
# elif plus_or_minus == '*':
#     print("The difference between the two numbers is ", num_1 * num_2 )
# elif plus_or_minus == '/':
#     print("The difference between the two numbers is ", num_1 / num_2 )



# for_7 = []
# for_5 = []

# for i in range(1500, 2701):
#     if i / 5:
#         for_5.append(i)
#     elif i / 7:
#         for_7.append(i)
    
# print(for_7)
# print(for_5)


# x= input('Enter letter: ')
# print(x[::-1])

# def first_last(string):
#     return string[-1] + string[1:-1] + string[0]

# def polindrome(arg):
#     if type(arg) == int:
#         arg = str(arg)
#     return arg == arg[::-1]
# print(polindrome(input('is polindrome: ')))



# [start : stop : step]
# def remove_nth_index(string, index):
#     return string[:index] + string[index + 1 :]



# def odd_index_toEnd_even_index_toStart(string): 
#     return string[::2] + string[1::2]
    
#     # string[::2] + string[::2]

# print(odd_index_toEnd_even_index_toStart('12345'))


# def first_last_two(string):
#     if len(string) < 2:
#         return ''
#     return string[:2] + string[-2:]

# def change_first_char(string:str, symbol='$') -> str:
#     first = string[0]
#     change = string.lower()
#     return first + change.replace(first.lower(), symbol)

# print(change_first_char('Hello HHH Hi Wow'))


def show_stars(num:int):
    stars = '*'
    if num == 1:
        print(stars)
    else:
        show_stars(num-1)
        print(stars * num)


show_stars(10)


# def shows_start_2(n):
#     print('*' * n)

#     if n > 1:
#         return shows_start_2(n-1)

# shows_start_2(10)


# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)
# print(factorial(5))
    


# def list_sum(num_List):
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
        
# print(list_sum([2, 4, 5, 6, 7]))