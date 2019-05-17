list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 8, 9, 5, 1, 7, 8, 5, 4, 0, 9, 1, 2, 3, 4, 6, 7, 8, 6, 5, 4, 1, 2, 67, 91, 15]
theSet = set([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 8, 9, 5, 1, 7, 8, 5, 4, 0, 9, 1, 2, 3, 4, 6, 7, 8, 6, 5, 4, 1, 2, 67, 91, 15])
print('Primary table:\t', list, '\n------------------------------------------------------------------------------')

#program prints only the first and last table's elements
def elements():
    list = []
    table = []
    for i in range(0, 151, 8):
        list.append(i)
    table.append(list[0])
    table.append(list[-1])
    print(table)

#power of 2
def powerTwo(n):
    a= 0
    b= 1
    while n > 0:
        print(b)
        a = b
        b = a+b
        n -= 1

#Fibonnaci
def fibonnaci(n):
    a= 0
    b= 1
    while n > 0:
        print(b)
        a, b= b,a+b #from left to right, before assigning a value
        n -= 1

#Delete duplicates from list
def delDuplicates(list):
    j = 0
    list.sort()
    temp = []
    for i in list:
        if i == 0:
            temp.append(i)
            i+=1
        elif i!=j:
            temp.append(i)
            j=i
    print(temp)

#Shorter version of delete duplicates
def delDuplicatesShort(lista):
    b = []
    for i in lista:
        if i not in b:
            b.append(i)
    print(b)

#delete duplicates from the set
def delDuplicatesSet(a):
    b = set()
    for i in a:
        if i not in b:
            b.add(i)
    print(a.intersection(b))

n = int(input("Set the number :\n>>>"))
print('-------------------------POWER OF TWO-----------------------------------')
powerTwo(n)
print('-------------------------FIBONNACI-----------------------------------')
fibonnaci(n)
print('-------------------------DELETE DUPLICATES-----------------------------------')
delDuplicates(list)
print('-------------------------DELETE DUPLICATES - SHORTER VERSION-----------------------------------')
delDuplicatesShort(list)
print('-------------------------DELETE DUPLICATES FROM THE SET-----------------------------------')
delDuplicatesSet(theSet)
print('-------------------------FIRST AND LAST ELEMENTS-----------------------------------')
elements()
