from card import Card
from deck import Deck

deck = Deck()
# for card in deck.cards: 
# 	print(str(card.number) + " of " + card.color)
deck.shuffle()

deck.print_deck()

print("\n")

hand = deck.draw(5)
for i in hand:
  print(str(i.number) + " of " + i.color)

print

deck.print_deck()

#card = Card("red", 3)
#print(card.color)