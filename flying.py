import decorator

class Flying(decorator.Decorator):
  '''A decorator that adds flying-related properties to a given monster.'''
  def __init__(self, monst):
    '''Initializes a new Flying object with a given Monster object.'''
    super().__init__(monst)
    monst._name = "Floating " + monst._name
    monst._hp += 15
        
  def attack(self):
    '''Overrides the attack method of the Monster object and returns the modified behavior with an additional flying-related attack bonus.'''
    return super().attack() + 2