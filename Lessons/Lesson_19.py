# ===============================================================================

# 10. Write a program that prints out the first 100 prime numbers.-  
# RU: Напишите программу, которая выводит первые 100 простых чисел.
def n_prime_numbers(n):
    pass


# ===============================================================================

# Напишите программу, которая вычисляет сумму первых 1000 чисел Фибоначчи.
# Напишите программу, которая печатает первые 1000 цифр PI (3.14).
# Напишите программу, которая генерирует случайный пароль длины 20.
# Write a program that calculates the factorial of a given number.
# Write a program that prints out the first 1000 perfect squares.
# Write a program that generates a random maze and solves it using the A* algorithm.
# Write a program that calculates the sum of the first 1000 prime numbers.
# Write a program that generates a random Sudoku puzzle and solves it.
# Write a program that calculates the sum of the first 1000 triangular numbers.

# ===============================================================================



# if __name__ == "__main__":
#     print(pattern(int(input("Enter a number: "))))

# ===============================================================================
# ===============================================================================

# num = range(1500, 2701)
# for i in num:
#     if (i % 7 == 0) and (i % 5 == 0):
#         print(i)
    
# ===============================================================================


# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
	
# ===============================================================================
# ===============================================================================

# even = []
# odd = []

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)


# print(f"Even : {len(even)}", f"Odd : {len(odd)}")

# ===============================================================================

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'} ]

# for i in datalist:
#     print(type(i))

# ===============================================================================


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# ===============================================================================

x,y = 0,1

while y < 50:
    print(y)
    x,y = y,x + y

# ===============================================================================