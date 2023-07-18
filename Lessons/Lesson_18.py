# mkdir => create a folder
# touch => create a file


with open('text.txt', 'w') as file:
    for item in range(100):
        file.write(str(item) + '\n')
    file.close()

inside = []

# ff = open('test.txt', 'r')
# print(ff.readline())
# ff.close()

# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num <= 3:
#         return True
#     elif num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
    
#     while i*i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# count = 0
# num = 2

# while count < 100:
#     if is_prime(num):
#         print(num)
#         count += 1
#     num += 1


# print(is_prime(101))


# Task 1: Write a program that asks the user to enter a number and checks if the number is even or odd. If it's even, print "The number is even." If it's odd, print "The number is odd."
# num = int(input("Enter a number"))
# if num % 2 == 0: 
#     print("The number is even.")
# else:
#     print("The number is odd." )

# Example Input: Enter a number: 6
# Example Output: The number is even.
# Task 2: Write a program that asks the user to enter two numbers and checks if the first number is greater than, less than, or equal to the second number. If it's greater than, print "The first number is greater than the second." If it's less than, print "The first number is less than the second." If it's equal to, print "The first number is equal to the second."
# Example Input: Enter the first number: 10 Enter the second number: 5
# Example Output: The first number is greater than the second.

# import csv
# with open('departments.csv', newline='') as file:
#  x = csv.reader(file, empty=' ', symbol='|')
#  for item in x:
#    print(', '.join(item))

