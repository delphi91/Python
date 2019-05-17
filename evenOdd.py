#program prints even and odd numbers of the list
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

print('List:', list, 'Length: ', list.__len__())
print('Even numbers:', sorted(even), 'Count: ', even.__len__())
print('Odd numbers:', sorted(odd), 'Count: ', odd.__len__())