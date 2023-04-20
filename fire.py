import decorator

class Fire(decorator.Decorator):
  '''A decorator that adds fire-related properties to a given monster.'''
  def __init__(self, monst):
    '''Initializes a new Fire object with a given Monster object.'''
    super().__init__(monst)
    monst._name = "Flaming " + monst._name
    monst._hp += 8
        
  def attack(self):
    '''Overrides the attack method of the Monster object and returns the modified behavior with an additional fire-related attack bonus.'''
    return super().attack() + 12