import decorator

class Flying(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name += " (Flying)"
    monst._hp += 20
        
  def attack(self):
    return super().attack() + 5