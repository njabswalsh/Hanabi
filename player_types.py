from collections import namedtuple

Action = namedtuple('Action', ['action_type', 'card_index'])

class PlayerState:
  def __init__(self, other_hands, hand_knowledge, hints_left, bombs_left, table):
    self.other_hands = other_hands
    self.hand_knowledge = hand_knowledge
    self.hints_left = hints_left
    self.bombs_left = bombs_left
    self.table = table