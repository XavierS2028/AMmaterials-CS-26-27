# RandomCard.py
import random

cardInt = random.randint(0, 51)

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

cardName = cards[cardInt % 13]
cardSuit = ""

if cardInt < 13:
    cardSuit = suits[0]
elif cardInt < 26:
    cardSuit = suits[1]
elif cardInt < 39:
    cardSuit = suits[2]
else:
    cardSuit = suits[3]

print(f"The card is {cardName} of {cardSuit}")