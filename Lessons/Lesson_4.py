
#!-------------------------------------------------------------------------------------------
#* isalnum()          Returns True if all characters in the string are alphanumeric
#*               RU: Возвращает True, если все символы в строке являются буквенно-цифровыми
#!-------------------------------------------------------------------------------------------
#* isalpha()       Returns True if all characters in the string are in the alphabet
#*               RU: Возвращает True, если все символы в строке находятся в алфавите
#!-------------------------------------------------------------------------------------------
#* isdecimal()      Returns True if all characters in the string are decimals
#*==             RU: Возвращает True, если все символы в строке являются десятичными
#!-------------------------------------------------------------------------------------------
#* isdigit()       Returns True if all characters in the string are digits
#*==             RU: Возвращает True, если все символы в строке являются цифрами
#!-------------------------------------------------------------------------------------------
#* isnumeric()      Returns True if all characters in the string are numeric
#*               RU: Возвращает True, если все символы в строке являются числовыми
#!-------------------------------------------------------------------------------------------
#* isspace()          Returns True if all characters in the string are whitespaces
#*               RU: Возвращает True, если все символы в строке являются пробелами
#!-------------------------------------------------------------------------------------------
#* join()          Joins the elements of an iterable to the end of the string
#*               RU: Объединяет элементы итерируемого объекта в конец строки
#!-------------------------------------------------------------------------------------------
#* ljust()          Returns a left justified version of the string  (==> padStart in JS)
#*               RU: Возвращает левую версию строки
#!-------------------------------------------------------------------------------------------
#* rjust()          Returns a right justified version of the string (==> padEnd in JS)
#*             RU: Возвращает правую версию строки
#!-------------------------------------------------------------------------------------------
#* strip()          Returns a trimmed version of the string         (==> trim in JS)
#*              RU: Возвращает усеченную версию строки
#!-------------------------------------------------------------------------------------------
#* replace()          Returns a string where a specified value is replaced with a specified value 
#*              RU: Возвращает строку, в которой указанное значение заменяется на указанное значение
#!-------------------------------------------------------------------------------------------
#* split()          Splits the string at the specified separator, and returns a list
#*              RU: Разделяет строку по указанному разделителю и возвращает список
#!-------------------------------------------------------------------------------------------
#* list()           For splitting string-letters into lists
#*              RU: Для разделения букв строки на списки
#*   EX: list('Hello') ==> ['H', 'e', 'l', 'l', 'o']
#!-------------------------------------------------------------------------------------------
#* rsplit(maxsplit)Splits the string at the specified separator, and returns a list
#*              RU: Разделяет строку по указанному разделителю и возвращает список  
#!-------------------------------------------------------------------------------------------
#* splitlines()     Splits the string at line breaks and returns a list
#*              RU: Разделяет строку по переводам строк и возвращает список
#!-------------------------------------------------------------------------------------------
#* zfill()          Fills the string with a specified number of 0 values at the beginning
#*              RU: Заполняет строку указанным количеством значений 0 в начале
#!-------------------------------------------------------------------------------------------
#* 'Hello'[::-1]    Reverses a string
#*              RU: Переворачивает строку
#!-------------------------------------------------------------------------------------------


#!------------------------------------------------
#* Bool   =>   bool()
#* ------------------------------------------------------------------
#* If / elif / else 
#* if 1==2:
#*     print(f'1 == 1 is => {1==2}')
#* elif 1==1:
#*     print(f'1 == 1 is => {1==1}')
#* else:
#*     print(1==2)
#! ------------------------------------------------------------------
#* match / case
#* HTTPS_status = 200
#* match HTTPS_status:
#*     case 200 | 201:
#*         print('OK')
#*     case 404:
#*         print('Not found')
#*     case 301 | 302:
#*         print('Redirect')
#*     case _:
#*         print('Unknown')
#! ------------------------------------------------------------------

#* EXERCISES
#* 1. Reverse and input from a user    &&    Reverse a number
#* RU: 
#*     Берите текст от клиента и выведите на терминале. 
#*     Найти зеркальное число.
#* inp = input("What is your name: ")
#* print(inp[::-1])
#* print(str(num)[::-1])
#* ----------------------------------------------------------
#* 2. Swap first and last digits of a number
#* RU: Поменяйте местами первую и последнюю цифры числа.
#* x = 123456789
#* x = str(x)
#* print(int(x[-1] + x[1:-1] + x[0]))
#* ----------------------------------------------------------
#* 3. check if a string is a palindrome

def is_polindrome(arg) -> bool:
    if type(arg) == int:
        arg = str(arg)
    # if isinstance(arg, int):
    #     arg = str(arg)
    return arg == arg[::-1]
print(is_polindrome(input('Guess a polindrome: ')))
# ----------------------------------------------------------

#* SOLUTIONS FOR PREVIOUS EXERCISES

#* print(str(num)[::-1])

#* print(input('Enter a number: ')[::-1])

#* print(str(num)[-1] + str(num)[1:-1] + str(num)[0])

#* print(str(num) == str(num)[::-1])