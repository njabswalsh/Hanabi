from table import Table
from hanabi_types import Action
from hanabi_types import PlayerState
from hanabi_types import *


def _get_cards_per_player(num_players):
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
  def __init__(self, deck, players, cards_per_player=None, hints_left=8, bombs_left=3):
    self.deck = deck
    self.table = Table(colors = deck.colors)
    self.players = players
    self.num_players = len(players)
    if cards_per_player:
      self.cards_per_player = cards_per_player
    else:
      self.cards_per_player = _get_cards_per_player(self.num_players)
    self.hints_left = hints_left
    self.bombs_left = bombs_left
    self.max_hints = hints_left
    self._setup_hands()
    self._setup_player_states()
    self.current_player = 0

  def _setup_hands(self):
    self.hands = []
    for i in range(self.num_players):
      self.hands.append(self.deck.draw(self.cards_per_player))

  def _setup_player_states(self):
    self.player_states = []
    for i in range(self.num_players):
      other_hands = {player_id: self.hands[player_id] for player_id in range(self.num_players) if i != player_id}
      self.player_states.append(PlayerState(other_hands, self.hints_left, self.bombs_left, self.table))

  def _update_player_states(self):
    for i in range(self.num_players):
      self.player_states[i].hints_left = self.hints_left
      self.player_states[i].bombs_left = self.bombs_left


  def _print_player_action(self, player_action):
    if player_action.action_type == ActionType.PLAY or player_action.action_type == ActionType.DISCARD:
      card = self.hands[self.current_player][player_action.card_index]
      print("Player {}: {} {}".format(self.current_player + 1, player_action.action_type.name, card))
    elif player_action.action_type == ActionType.HINT:
      hint = player_action.hint
      if hint.hint_type == HintType.COLOR:
        hint_info = self.hands[hint.to_player_id][hint.card_indices[0]].color
      else:
        hint_info = self.hands[hint.to_player_id][hint.card_indices[0]].number
      print("Player {} hints Player {}: You have {} {} in spots {}".format(
          hint.from_player_id + 1, hint.to_player_id + 1, len(hint.card_indices), hint_info, hint.card_indices))
  
  def _print_game_state(self):
    self.table.print_state()
    print("Hints left: {}".format(self.hints_left))
    print("Bombs left: {}".format(self.bombs_left))
  
  def play_game(self, verbose=False):
    if verbose:
      self.table.print_state()
    while self.deck.cards_left() > 0:
      self.play_turn(verbose=verbose)
      if verbose:
        self._print_game_state()
      if self.bombs_left == 0:
        if verbose:
          print("All bombs are gone. Game over.")
          print("Cards played: {}".format(self.table.num_cards_played()))
        return
    if verbose:
      print("All cards in the deck are gone.")
    for i in range(self.num_players):
      self.play_turn(verbose=verbose)
      if verbose:
        self._print_game_state()
    if verbose:
      print("Ran out of cards. Game over")
      print("Cards played: {}".format(self.table.num_cards_played()))

  def play_turn(self, verbose=False):
    player_action = self.players[self.current_player].play(self.player_states[self.current_player])
    if verbose:
      self._print_player_action(player_action)
    if player_action.action_type == ActionType.PLAY:
      card_index = player_action.card_index
      played_card = self.hands[self.current_player][card_index]
      card_playable = self.table.play(played_card)
      if not card_playable:
        self.bombs_left -= 1
      elif played_card.number == 5:
        self.hints_left += 1
      self.hands[self.current_player].pop(card_index)
      self.hands[self.current_player] += self.deck.draw(1)
    elif player_action.action_type == ActionType.DISCARD:
      if self.hints_left == self.max_hints:
        raise Exception("Illegal Play: Cannot discard when all hints are available.")
      card_index = player_action.card_index
      self.table.discard(self.hands[self.current_player][card_index])
      self.hands[self.current_player].pop(card_index)
      self.hands[self.current_player] += self.deck.draw(1)
      self.hints_left += 1
    elif player_action.action_type == ActionType.HINT:
      if self.hints_left == 0:
        raise Exception("Illegal Play: Cannot hint when no hints are available.")
      for player in self.players:
        player.hint(player_action.hint)
      self.hints_left -= 1
    else:
      raise Exception("Unsupported action: " + player_action.action_type)
    # Move to next player
    self.current_player += 1
    self.current_player = self.current_player % self.num_players
    self._update_player_states()
