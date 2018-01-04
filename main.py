from card import Card
from deck import Deck

deck = Deck()
for card in deck.cards: 
	print(str(card.number) + " of " + card.color)

#card = Card("red", 3)
#print(card.color)