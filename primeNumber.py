#Checking that the user number is prime or not

userNumber = input('Set the number:\n>>>\t ')
userNumber = int(userNumber)

dividers = []

for number in range(1, userNumber + 1, 1):
    if(userNumber % number == 0):
        dividers.append(number)

if len(dividers) == 2 or userNumber == 1:
    print('The number', userNumber, 'is prime!')
else:
    print('The number', userNumber, 'is not prime')