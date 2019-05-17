#quadratic function - need to instal matplotlib and numpy package
import math
import matplotlib.pyplot as plt
import numpy as np

def qFunction(a, b, c):

    plt.figure(figsize=(10, 9), dpi=100)

    print(a,'x^2 + ',b,'x + ', c,' = 0')
    x = np.arange(-10, 10, 0.1)

    delta = (b**2)-4*a*c
    y = a*(x**2)+b*x+c

    if delta > 0:
        print('Delta = ', delta)
        x1=((-b)- (math.sqrt(delta)))//2*a
        x2=((-b)+ (math.sqrt(delta)))//2*a

        print('x =',x1,' or\t x =',x2)

        plt.xlabel('Axis X')
        plt.ylabel('Axis Y')
        plt.axvline(x=0, color="#000000")
        plt.axhline(y=0, color="#000000")
        plt.title('a*x^2+b*x+c')
        plt.plot(x, y)
        plt.show()

    elif delta == 0:
        print('Delta =', delta)
        x0 = (-b)//2*a

        print('x = ', x0)
        plt.xlabel('Axis X')
        plt.ylabel('Axis Y')
        plt.axhline(y=0, color="#000000")
        plt.axvline(x=0, color="#000000")
        plt.title('a*x^2+b*x+c')
        plt.plot(x, y)
        plt.show()

    else:
        print('Delta = ', delta,'. No roots.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(y=0, color="#000000")
        plt.axvline(x=0, color="#000000")
        plt.title('a*x^2+b*x+c')
        plt.plot(x, y)
        plt.show()

print('a*x^2 + b*x + c\n')
a = input("Set a\n")
b = input('Set b\n')
c = input('Set c\n')

a=int(a)
b=int(b)
c=int(c)

qFunction(a, b, c)