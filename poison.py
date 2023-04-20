import decorator
class Poison(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    self._name += " (Poison)"
    self._hp += 15
        
  def attack(self):
    return super().attack() + 7