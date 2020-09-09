from card import Card
import random

class Deck:
  colors = ["red", "blue", "green", "yellow", "white"]
  numbers = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]

  def __init__(self):
    self.cards = []
    self.fill_deck()

  def fill_deck(self):
    for color in self.colors:
      for number in self.numbers:
        self.cards.append(Card(color, number))

  def shuffle(self):
    random.shuffle(self.cards)

  def draw(self, number):
    ret = []
    for i in range(number):
      ret.append(self.cards.pop())
    return ret

  def print_deck(self):
    for card in self.cards:
      print(card)