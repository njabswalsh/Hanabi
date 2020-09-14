from card import Card
from deck import Deck
from table import Table
from game_manager import GameManager
from players import SimplePlayer
from players import BasicPlayer

deck = Deck()
deck.shuffle()
num_players = 2
players = [BasicPlayer(i, num_cards=5) for i in range(num_players)]

gm = GameManager(deck, players)

gm.play_game(verbose=True)
