class Card:
  def __init__(self, color, number):
    self.color = color
    self.number = number

  def __str__(self):
    return (str(self.number) + " of " + self.color.capitalize())