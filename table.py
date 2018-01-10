class Table:
  def __init__(self, played=None, discarded=None):
    # if(played)
    #   self.played = played
    # else
    self.played = {"red":0,"green":0,"blue":0,"brown":0,"purple":0}
    # if(discarded)
    #   self.discarded = discarded
    # else
    self.discarded = {}

  # Returns 1 if card is playable, 0 otherwise
  def play_card(self, card):
    if (self.is_playable(card)):
      self.played[card.color] += 1 
      return 1
    else:
      return 0 
    
  def print_state(self):
    print("Played:")
    for key in self.played:
      print(str(self.played[key]) + " of " + key)

  def is_playable(self, card):
    playable = False
    if (self.played[card.color] == card.number - 1):
      playable = True  
    return playable
