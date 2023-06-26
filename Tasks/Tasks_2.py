
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