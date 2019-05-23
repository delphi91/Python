#program prints even and odd numbers of the list
import random
def evenOddList():
    list = [1, 6, 2, 8, 3 , 4, 56, 745, 221, 9, 64354, 2235, 78532, 6643, 12345, 32, 11, 22, 445, 667, 88]
    temp = []
    even = []
    odd = []
    for number in list:
        if number not in temp:
            temp.append(number)
    for number in temp:
        if ( number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)

    print('Static list:', list, 'Length: ', list.__len__())
    print('Even numbers:', sorted(even), 'Count: ', even.__len__())
    print('Odd numbers:', sorted(odd), 'Count: ', odd.__len__())
#program prints even and odd numbers of random numbers
def evenOddrandom():
    list = []
    for i in random.sample(range(0,100),21):
        list.append(i)
    temp = []
    even = []
    odd = []
    for number in list:
        if number not in temp:
            temp.append(number)
    for number in temp:
        if (number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    print('Dynamic list:', list, 'Length: ', list.__len__())
    print('Even numbers:', sorted(even), 'Count: ', even.__len__())
    print('Odd numbers:', sorted(odd), 'Count: ', odd.__len__())

def evenOdd():
    data = []
    for i in random.sample(range(0,100),21):
        data.append(i)
    odd = []
    even = []
    for n in data:
        if n % 2:
            odd.append(n)
        else:
            even.append(n)
    print(f'Primary table: {data}')
    print(f'Odd numbers: {odd}')
    print(f'Even number {even}')

def isOdd(x):
    return x %2

evenOddList()
print('\n-------------------------------------------------------\n')
evenOddrandom()
print('\n-------------------------------------------------------\n')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('Static list: ',data)
data = filter(isOdd, data)
data = list(data)
print('Odd numbers: ',data)
print('\n-------------------------------------------------------\n')
evenOdd()