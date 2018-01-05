from card import Card

class Deck:
  colors = ["red", "blue", "green", "purple", "brown"]
  numbers = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]

  def __init__(self):
    self.cards = []
    self.fill_deck()

  def fill_deck(self):
    for color in self.colors:
      for number in self.numbers:
        self.cards.append(Card(color, number))