#Guess the number
import random
number = random.randint(1, 9)
counter = 1
userNumber = 0
print('Guess the number 1-9\n')

while userNumber!=number:
    userNumber = input()
    userNumber = int(userNumber)
    if userNumber<number:
        print('Too less, try again...')
        counter+=1
    elif userNumber>number:
        print('Too much, try again...')
        counter+=1
print('Correct! Counter = ', counter)