# Chris
from monster import Monster

class Undead(Monster):
  ''' Represents a constructed monster (Beast) '''
  def __init__(self):
    super().__init__("Undead", 8)

  def attack(self):
    ''' Returns base attack power '''
    return 8