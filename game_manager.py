from table import Table
from player_types import Action
from player_types import PlayerState


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
      self.player_states.append(PlayerState([], [], self.hints_left, self.bombs_left, self.table))

  def print_player_action(self, player_action):
    if player_action.action_type == "play" or player_action.action_type == "discard":
      card = self.hands[self.current_player][player_action.card_index]
      print("Player {}: {} {}".format(self.current_player + 1, player_action.action_type, card))
    else:
      # TODO: Print hints
      pass

  def play_game(self, verbose=False):
    if verbose:
      self.table.print_state()
    while self.deck.cards_left() > 0:
      self.play_turn(verbose=verbose)
      if verbose:
        self.table.print_state()

  def play_turn(self, verbose=False):
    player_action = self.players[self.current_player].play()
    if verbose:
      self.print_player_action(player_action)
    if player_action.action_type == "play":
      #TODO: Bombs
      card_index = player_action.card_index
      self.table.play(self.hands[self.current_player][card_index])
      self.hands[self.current_player].pop(card_index)
      self.hands[self.current_player] += self.deck.draw(1)
    elif player_action.action_type == "discard":
      card_index = player_action.card_index
      self.table.discard(self.hands[self.current_player][card_index])
      self.hands[self.current_player].pop(card_index)
      self.hands[self.current_player] += self.deck.draw(1)
      self.hints_left += 1
      # TODO: Use max hints to limit when you can discard
    else:
      print("Unsupported action:", player_action.action_type)
    # Move to next player
    self.current_player += 1
    self.current_player = self.current_player % self.num_players

