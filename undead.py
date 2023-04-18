# Chris
from monster import Monster

class Undead(Monster):
  def __init__(self):
    super().__init__("Undead", 8)

  def attack(self):
    return 8