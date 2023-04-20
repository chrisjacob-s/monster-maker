import decorator

class Lasers(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    self._name += " (Laser)"
    self._hp += 5
        
  def attack(self):
    return super().attack() + 15