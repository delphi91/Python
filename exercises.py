#Calendar
import calendar as cr
print(cr.month(2016,2))
year = input('Enter the year:\n>>> ')
month = input('Enter the month number:\n>>> ')
calendar = cr.month(int(year), int(month))
print(calendar)

#Print 10 stars: **********
#1 method
print("*"*10)
#2 method
x = 0
while(x < 10):
    print("*", end='')
    x+=1
print('\n')
#3 method
for i in range(1,11):
    print('*'*i)
print('\n')
#4 method
for i in range(1,11):
    print('*',end='')

#Print numbers from 20 to 1
for i in range(20,-1,-1):
    print(i, ', ', end='')