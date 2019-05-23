my_list1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 8, 9, 5, 1, 7, 8, 5, 4, 0, 9, 1, 2, 3, 4, 6, 7, 8, 6, 5, 4, 1, 2, 67, 91, 15]
theSet = set([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 8, 9, 5, 1, 7, 8, 5, 4, 0, 9, 1, 2, 3, 4, 6, 7, 8, 6, 5, 4, 1, 2, 67, 91, 15])
my_list2 = ['a', 'b', 'c', 'd', 'a', 'b', 'a', 'b', 'c', 'c', 'a', ' a', ' b', 'ab', 'c', 'b','b']
word = 'Höllenhund'
print('Primary table:\t', my_list1, '\n------------------------------------------------------------------------------')

#program prints only the first and last table's elements
def elements():
    my_list = []
    table = []
    for i in range(0, 151, 8):
        my_list.append(i)
    table.append(my_list[0])
    table.append(my_list[-1])
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
def delDuplicates(my_list):
    j = 0
    my_list.sort()
    temp = []
    for i in my_list:
        if i == 0:
            temp.append(i)
            i+=1
        elif i!=j:
            temp.append(i)
            j=i
    print(temp)

#Shorter version of delete duplicates
def delDuplicatesShort(my_list):
    b = []
    for i in my_list:
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

def removeChr(w):
    import unidecode
    print('Before decode:\t',w)
    w = unidecode.unidecode(w)
    print('After decode:\t',w)

def counterElements(my_list):
    for i in sorted((set(my_list))):
        count = my_list.count(i)
        print(f'{i} = {count} times')

n = int(input("Set the number :\n>>>"))
print('-------------------------POWER OF TWO-----------------------------------')
powerTwo(n)
print('-------------------------FIBONNACI-----------------------------------')
fibonnaci(n)
print('-------------------------DELETE DUPLICATES-----------------------------------')
delDuplicates(my_list1)
print('-------------------------DELETE DUPLICATES - SHORTER VERSION-----------------------------------')
delDuplicatesShort(my_list1)
print('-------------------------DELETE DUPLICATES FROM THE SET-----------------------------------')
delDuplicatesSet(theSet)
print('-------------------------FIRST AND LAST ELEMENTS-----------------------------------')
elements()
print('-------------------------REMOVE ACCENTS FROM THE WORD-----------------------------------')
removeChr(word)
print('-------------------------COUNT ELEMENTS IN LIST-----------------------------------')
counterElements(my_list2)