# Chris
from monster import Monster

class Alien(Monster):
  ''' Represents a constructed monster (Alien) '''
  def __init__(self):
    super().__init__("Alien", 5)

  def attack(self):
    ''' Returns base attack power '''
    return 10
  