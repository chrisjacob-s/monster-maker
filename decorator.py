import monster
import abc

class Decorator(monster.Monster, abc.ABC):
  def __init__(self, monster):
    super().__init__(monster.name, monster.hp)
    self._monster = monster
        
  def attack(self):
    return self._monster.attack()