#program prints two lists common numbers
a = [1, 2, 3, 5, 8, 3, 5, 24, 7, 8, 2]
b = [1, 5, 7, 9, 12, 24, 2, 1, 90, 4, 2, 4, 7, 8]

temp = []
final = []
for number in a:
    if number in b:
        temp.append(number)

    for x in temp:
        if x not in final:
            final.append(x)
print(sorted(a),'\n',sorted(b))
print('Final:\n',sorted(final))