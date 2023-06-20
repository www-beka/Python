# mkdir => create a folder
# touch => create a file

# ff = open('test.txt', 'a')
# ff.write('some text')
# ff.close()

# ff = open('test.txt', 'r')
# print(ff.readline())
# ff.close()

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    
    while i*i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
num = 2

while count < 100:
    if is_prime(num):
        print(num)
        count += 1
    num += 1


print(is_prime(101))
