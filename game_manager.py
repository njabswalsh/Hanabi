from collections import namedtuple

PlayerState = namedtuple('PlayerState', ['other_hands', 'hand_knowledge', 'hints_available', 'cards_played', 'cards_discarded'])

def _get_cards_per_player(self, num_players):
  if num_players == 2:
    return 5
  if num_players == 3:
    return 5
  if num_players == 4:
    return 4
  if num_players == 5:
    return 4
  raise ValueError('Invalid number of players: ' + str(num_players))

class GameManager:
  def __init__(self, deck, players, cards_per_player=None, hints_available=8, bombs_available=3):
    self.deck = deck
    self.num_players = len(players)
    if cards_per_player:
      self.cards_per_player = cards_per_player
    else:
      self.cards_per_player = _get_cards_per_player(self.num_players)
    self.hints_available = hints_available
    self.bombs_available = bombs_available
    self._setup_hands()

  def _setup_hands(self):
    for i in range(self.num_players):
      self.hands.append(self.deck.draw(self.cards_per_player))

  def play_game(self):

  def play_turn(self):
