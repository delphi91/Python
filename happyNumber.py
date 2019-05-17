#Program check that user number is happy

def happyNumber(a):

    b = int(a)**2
    tab = []
    while b != 1:
        if b < 9:
            b=b**2
        else:
            temp = str(b)
            b = 0
            list = []
            for i in temp:
                list.append(i)
            for j in list:
                b=b+int(j)**2
        tab.append(b)
        tab.sort()
        for y in tab:
            if tab.count(y)>1:
                print(a, ' not the happy number :(')
                exit()
    print(a, 'happy number! :)')


print('------Checking happy number------\n')
a = input('Set the number:\n>>>\t')
happyNumber(a)



