import random
list = []
while len(list) < 6:
    number = random.randint(1, 49)

    if number in list:
        continue
    list.append(number)
print('Your lucky numbers: ',list)