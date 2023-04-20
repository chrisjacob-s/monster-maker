import decorator

class Poison(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name += " (Poison)"
    monst._hp += 15
        
  def attack(self):
    return super().attack() + 7