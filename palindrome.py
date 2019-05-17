#program check taht the word is a palindrome or not

sentence = input('Write the word or sentence: ')
sentence = sentence.lower()
palindrome = sentence[::-1]

print(sentence)
print(palindrome)

if(sentence == palindrome):
    print('This is a palindrome!')
else:
    print('It\'s not a palindrome')
