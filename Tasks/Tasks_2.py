
#!=============================================================
a = 'Hello Wolrd'
# print(len(a))
#!=============================================================
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
# print(char_frequency('google.com'))
#!=============================================================

def second_most_frequent(string): # второй_наиболее_часто_встречающийся
    dict = {}
    for i in string:
        dict[i] = string.count(i)
        print(string.count(i))
    # return sorted(dict.items(), key=lambda x: x[1])[-2][0]
    

print(second_most_frequent('Hello World'))

#!=============================================================

# import random


# def pick_word():
#     with open("sowpods.txt", "r") as f:
#         words = f.readlines()
#     return random.choice(words).strip()


# def guess_letters():
#     word = pick_word()
#     guessed = "_" * len(word)
#     word = list(word)
#     guessed = list(guessed)
#     lstGuessed = []
#     letter = input("Guess letter: ")
#     tries = 0
#     while True:
#         if letter.upper() in lstGuessed:
#             letter = ''
#             print("Already guessed!!")
#         elif letter.upper() in word:
#             index = word.index(letter.upper())
#             guessed[index] = letter.upper()
#             word[index] = '_'
#             print("Well guessed!!")
#         else:
#             tries += 1
#             print(f"Wrong!! You have {6 - tries} tries left")

#         print(''.join(guessed))
#         if letter != '':
#             lstGuessed.append(letter.upper())

#         letter = input("Guess letter: ")

#         if '_' not in guessed:
#             print("You won!!")
#             break
#         elif tries == 6:
#             print("You lost!!")
#             break


# guess_letters()


import random
import string

def generate_random_letters(length):
    letters = string.ascii_letters  # Uppercase and lowercase letters
    random_letters = ''.join(random.choice(letters) for _ in range(length))
    return random_letters

random_string = generate_random_letters(100)
print(random_string)