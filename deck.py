from card import Card

class Deck:
	def __init__(self):
		self.cards = []
		self.colors = ["red", "blue"]
		self.numbers = [1, 2, 3, 4, 5]
		self.fill_deck()

	def fill_deck(self):
		for color in self.colors:
			for number in self.numbers:
				self.cards.append(Card(color, number))