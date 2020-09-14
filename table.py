class Table:
  def __init__(self, played=None, discarded=None, colors=["red", "blue", "green", "yellow", "white"]):
    # if(played)
    #   self.played = played
    # else
    self.played =  {color : 0 for color in colors}
    # if(discarded)
    #   self.discarded = discarded
    # else
    self.discarded = {color : [] for color in colors}

  def print_state(self):
    print("Played:")
    for key in self.played:
      print(str(self.played[key]) + " of " + key)
    print 
    print("Discarded: ")
    for key in self.discarded:
      print(key + ": {}".format(self.discarded[key]))
      print

  # Returns True if card is playable, False otherwise
  def play(self, card):
    if (self.is_playable(card)):
      self.played[card.color] += 1 
      return True
    else:
      self.discard(card)
      return False 

  def is_playable(self, card):
    playable = False
    if (self.played[card.color] == card.number - 1):
      playable = True  
    return playable

  def discard(self, card):
    card_color = card.color
    array = self.discarded[card_color]
    array.append(card.number)
    array.sort()

  def num_cards_played(self):
    return sum(num_played for color, num_played in self.played.items())
