from card import Card
from hanabi_types import Action
from hanabi_types import ActionType
from player_utils import *

class SimplePlayer:
  def __init__(self):
    pass

  def play(self, state):
    return Action(ActionType.PLAY, 0, None)

  def hint(self, hint):
    pass

class BasicPlayer():
  def __init__(self, player_id, num_cards=5, max_hints=8):
    self.player_id = player_id
    self.playable_cards = []
    self.num_cards = num_cards
    self.max_hints = max_hints

  def _get_first_possible_hint(self, state):
    # TODO: Deal with player ids
    for to_player_id, hand in state.other_hands.items():
      for i in range(len(hand)):
        if state.table.is_playable(hand[i]):
          hintable, hint_type = is_hintable(i, hand)
          if hintable:
            return construct_hint(i, hand, to_player_id, self.player_id, hint_type)
    return None

  def play(self, state):
    if len(self.playable_cards) > 0:
      playable_card = self.playable_cards[0]
      self.playable_cards.pop(0)
      return Action(ActionType.PLAY, playable_card, None)
    first_possible_hint = self._get_first_possible_hint(state)
    if state.hints_left > 0 and first_possible_hint:
      return Action(ActionType.HINT, 0, first_possible_hint)
    elif state.hints_left < self.max_hints:
      return Action(ActionType.DISCARD, self.num_cards - 1, None)
    else:
      return Action(ActionType.PLAY, self.num_cards - 1, None)

  def hint(self, hint):
    if hint.to_player_id == self.player_id:
      self.playable_cards.append(hint.card_indices[0])