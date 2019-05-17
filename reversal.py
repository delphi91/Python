#reversal words or sentence
def reversal(slowo):
    return " ".join(slowo.split(' ')[::-1])

words = input("Write some words or sentence\n>>>\t")
print(reversal(words))