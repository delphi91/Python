#The program prints the divisors of the user number

userNumber = input('Set a number: ')
userNumber = int(userNumber)

dividers = []

for number in range(1, userNumber + 1, 1):
    if(userNumber % number == 0):
        dividers.append(number)

print('Dividers list of number', userNumber, ':\n', dividers)