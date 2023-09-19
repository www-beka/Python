# -----------------------------------
# `${......}` => String template  => JS
#  f{......}  => f string         => Python
# -----------------------------------
# a, b, c = [1, 2, 3]
# print(a, b, c, sep="-")



num_1 = int(input('Enter first number:'))
num_2 = int(input('Enter second number:'))
plus_or_minus = input('Enter symbol:')

if plus_or_minus == '+':
    print("The sum of two numbers is", num_1 + num_2)
elif plus_or_minus == '-':
    print("The difference between the two numbers is ", num_1 - num_2)
elif plus_or_minus == '*':
    print("The difference between the two numbers is ", num_1 * num_2 )
elif plus_or_minus == '/':
    print("The difference between the two numbers is ", num_1 / num_2 )

