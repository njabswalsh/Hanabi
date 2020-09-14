from hanabi_types import Action
from hanabi_types import ActionType
from hanabi_types import Hint
from hanabi_types import HintType

def construct_hint(card_index, hand, to_player_id, from_player_id, hint_type):
  if hint_type == HintType.COLOR:
    color = hand[card_index].color
    card_indices = [i for i in range(len(hand)) if hand[i].color == color]
  elif hint_type == HintType.NUMBER:
    number = hand[card_index].number
    card_indices = [i for i in range(len(hand)) if hand[i].number == number]
  return Hint(from_player_id, to_player_id, card_indices, hint_type)

def is_hintable(card_index, hand):
  hint_card = hand[card_index]
  color_hint_possible = True
  number_hint_possible = True
  for i in range(card_index):
    if hand[i].color == hint_card.color:
      color_hint_possible = False
    if hand[i].number == hint_card.number:
      number_hint_possible = False
  if color_hint_possible:
    return True, HintType.COLOR
  if number_hint_possible:
    return True, HintType.NUMBER
  return False, None

# Assumes that there are 3 of each 1, 2 of each 2, 3, 4, and 1 of each 5
def is_crucial(card, table):
  if card.number == 5:
    return True
  discarded = table.discarded[card.color]
  if card.number == 1:
    return discarded.count(1) == 2
  else:
    return card.number in discarded
