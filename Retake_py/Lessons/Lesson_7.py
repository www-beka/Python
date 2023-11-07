def remove_item(set1:set, *args):
    return set1.difference(args)


from time import sleep

x = 'hello world'
arr = ['a', 'b', 'c', 'd','e','f','g','h','i','j',
       'k','l','m','n','o','p','r','s','t','u',
       'v','y','w','q','z',' ']
z = 0
t = ''
while t != x:
    for i in arr:
        if t == x:
            break
        print(t+i, end='\r')
        if i == x[z]:
            t += i
            z += 1
            sleep(0.3)
            break
        sleep(0.1)