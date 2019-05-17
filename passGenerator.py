import random
import string
#password generator
def generator():
    strenght = input('How strong password you need?\n 1 - Weak\n 2 - Medium\n 3 - Strong\n>>>\t')
    strenght = int(strenght)

    signs = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    if strenght == 1:
        password = random.sample(signs, 7)
        random.shuffle(password)
        for i in password:
            password = ''.join(password)
        print(password)
    elif strenght == 2:
        password = random.sample(signs, 10)
        random.shuffle(password)
        for i in password:
            password = ''.join(password)
        print(password)
    elif strenght == 3:
        password = random.sample(signs, 20)
        random.shuffle(password)
        for i in password:
            password = ''.join(password)
        print(password)

generator()