from card import Card
from deck import Deck
from table import Table
from game_manager import GameManager
from players import SimplePlayer

deck = Deck()
deck.shuffle()
num_players = 2
players = [SimplePlayer() for i in range(num_players)]

gm = GameManager(deck, players)

gm.play_game(verbose=True)
