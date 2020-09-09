from card import Card
from deck import Deck
from table import Table

deck = Deck()

deck.shuffle()

deck.print_deck()

print("\n")

hand = deck.draw(5)
for i in hand:
  print(i)

print

deck.print_deck()

print("TABLE STUFF")
table = Table()
table.print_state()
print
one_of_yellow = Card("yellow",1)
table.play(one_of_yellow)
table.discard(one_of_yellow)
for card in hand:
  table.discard(card)
table.print_state()
#card = Card("red", 3)
#print(card.color)