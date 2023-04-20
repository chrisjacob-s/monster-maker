import decorator

class Lasers(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name += " with Lasers"
    monst._hp += 2
        
  def attack(self):
    return super().attack() + 15