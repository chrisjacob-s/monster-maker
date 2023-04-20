# Chris
from monster import Monster

class Beast(Monster):
  ''' Represents a constructed monster (Beast) '''
  def __init__(self):
    super().__init__("Beast", 10)

  def attack(self):
    ''' Returns base attack power '''
    return 5