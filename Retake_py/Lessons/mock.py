def insert_string_middle(string, string_to_insert):
    return string[:len(string) // 2] + string_to_insert + string[len(string) // 2:]

def first_three(string):
    return string[0:3]

def first_half_even(string):
    if len(string) % 2 == 0:
        return string[:len(string) // 2]
    return string

print(first_half_even('Bekzod'))

def concant_string(string1, string2):
    return str(string1) + str(string2)


def remove_indentation(string):
    return str(string).replace(' ', '')

def count_vowels(string):
    v = 'aeiou'
    counter = 0
    
    for i in string:
        i = i.lower()
        if i in v:
            counter = counter+1
    return counter     

def swap_case(string):
    return str(string).swapcase()

def chek_dublcate_letters(string) -> bool:
    for letter in string:
        index_of_letter = string.index(letter)
        if string[index_of_letter-1] == letter or string[index_of_letter+1]:
            return True
    return False



def piramid(star):
    if star == 1:
        return "*"
    else:
        return "*" * star,'\n' + piramid(star-1)

print(piramid(10))

# def show_stars(num:int):
#     stars = '*'
#     if num == 1:
#         print(stars)
#     else:
#         show_stars(num-1)
#         print(stars * num)


# show_stars(10)

