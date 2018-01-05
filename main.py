from card import Card
from deck import Deck

deck = Deck()

deck.shuffle()

deck.print_deck()

print("\n")

hand = deck.draw(5)
for i in hand:
  print(i)

print

deck.print_deck()

#card = Card("red", 3)
#print(card.color)