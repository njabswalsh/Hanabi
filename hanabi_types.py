from collections import namedtuple
from enum import Enum

class HintType(Enum):
  COLOR = 1
  NUMBER = 2

class ActionType(Enum):
  PLAY = 1
  DISCARD = 2
  HINT = 3

Action = namedtuple('Action', ['action_type', 'card_index', 'hint'])
Hint = namedtuple('Hint', ['from_player_id', 'to_player_id', 'card_indices', 'hint_type'])

class PlayerState:
  def __init__(self, other_hands, hints_left, bombs_left, table):
    self.other_hands = other_hands
    self.hints_left = hints_left
    self.bombs_left = bombs_left
    self.table = table