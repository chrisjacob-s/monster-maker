import decorator

class Fire(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name += " (Fire)"
    monst._hp += 10
        
  def attack(self):
    return super().attack() + 10