#Program prints numbers from list smaller than 5

list = [1, 5, 2, 1, 4, 7, 8, 99, 3, 55, 22, 33, 421, 68, 12, 1, 3, 9, 3]
newList =[]
userList = []
listLength = list.__len__()
count = 0
for number in list:
    if(number<5):
        newList.append(number)

print('List length: ', listLength)
print('Numbers less than 5:', newList)

userNumber = input('Smaller than which value you want to write numbers?')
userNumber = int(userNumber)

for number in list:
    if(number<userNumber):
        userList.append(number)
        count+=1

print('Written out ', count, 'numbers of', listLength)
if(userList.__len__()== 0):
    print('No elements!')
else:
    print(userList)