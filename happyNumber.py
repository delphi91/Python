#Program check that user number is happy

def happyNumber(a):
    a = int(a)
    if a == 0:
        print(a, 'Not happy :(')
    if a == 1:
        print(a, 'Happy!')
    list = []
    number = a
    while number != 1:
        if number < 9:
            number = number ** 2
            list.append(number)
        else:
            number = str(number)
            temp = []
            for j in number:
                temp.append(j)
            number = 0

            for t in temp:
                number = number + int(t) ** 2
            list.append(number)
            if list.count(number) > 1:
                print(a, 'Not Happy :(')
                break
            for l in list:
                if l == 1:
                    print(a, 'Happy!:)')

#saving to files- list of random numbers
def happyNumbers():
    happyFile = open('happy.txt', 'w+')
    happyFile.write('File with happy numbers:\n')
    sadFile = open('sad.txt', 'w+')
    sadFile.write('File with not happy numbers:\n')
    for i in range(0,41):
        if i ==1:
            print(i, ':D')
            happyFile.write(str(i)+', ')
        if i == 0:
            print(i, ':<')
            sadFile.write(str(i)+', ')
            i+=1
        list = []
        number = i
        while number !=1:
            if number <9:
                number = number**2
                list.append(number)
            else:
                number = str(number)
                temp = []
                for j in number:
                    temp.append(j)
                number = 0

                for t in temp:
                    number = number + int(t)**2
                list.append(number)
                if list.count(number)>1:
                    print(i, ':<')
                    sadFile.write(str(i)+', ')
                    break
                for l in list:
                    if l ==1:
                        print(i, ':D')
                        happyFile.write(str(i)+', ')
    sadFile.close()
    happyFile.close()
print('------Checking happy number------\n')
a = input('Set the number:\n>>>\t')
happyNumber(a)
happyNumbers()
