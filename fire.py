import decorator

class Fire(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name = "Flaming " + monst._name
    monst._hp += 8
        
  def attack(self):
    return super().attack() + 12