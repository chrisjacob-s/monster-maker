# Chris
from monster import Monster

class Alien(Monster):
  def __init__(self):
    super().__init__("Alien", 5)

  def attack(self):
    return 10
  