# Chris
from monster import Monster

class Beast(Monster):
  def __init__(self):
    super().__init__("Beast", 10)

  def attack(self):
    return 5