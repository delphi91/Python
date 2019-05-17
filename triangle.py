#The pascal Triangle - 7 levels
width = 60
level = 7
numbers = [1]

def pascalTriangle():
    line = ''
    for n in numbers:
        line += "%3d " % (n)
    print(line.center(width))

pascalTriangle()
for i in range(level - 1):
    newNumber = [1]
    position = 0
    while position < len(numbers)-1:
        newNumber.append(numbers[position] + numbers[position + 1])
        position+=1
    newNumber.append(1)
    numbers = newNumber.copy()
    pascalTriangle()
