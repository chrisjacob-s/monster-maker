import decorator

class Flying(decorator.Decorator):
  def __init__(self, monst):
    super().__init__(monst)
    monst._name = "Floating " + monst._name
    monst._hp += 15
        
  def attack(self):
    return super().attack() + 2