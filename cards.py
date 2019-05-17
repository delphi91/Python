#Two ways to playing cards
import random

colors = ['Heart', 'Club', 'Diamond', 'Spade']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
deckOfCards = []

for figure in figures:
    for color in colors:
        deckOfCards.append(figure + ' ' + color)

print(deckOfCards)
random.shuffle(deckOfCards)
print(deckOfCards)

playerOne = []
playerTwo = []

max = len(deckOfCards)
print(max/2)
for i in range(max):
    if i % 2 == 0:
        playerOne.append(deckOfCards[i])
    else:
        playerTwo.append(deckOfCards[i])
print('\n\n--------------------- PLAYER ONE ---------------------')
print(playerOne)
print('--------------------- PLAYER TWO ---------------------')
print(playerTwo)
print('\n------------------------------------------------------------------------------------------------------\n')
playerOne = deckOfCards[:26]
playerTwo = deckOfCards[26:]
print('--------------------- PLAYER ONE ---------------------')
print(playerOne)
print('--------------------- PLAYER TWO ---------------------')
print(playerTwo)