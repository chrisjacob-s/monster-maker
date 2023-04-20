import decorator

class Poison(decorator.Decorator):
  '''A decorator that adds poison-related properties to a given monster.'''
  def __init__(self, monst):
    '''Initializes a new Poison object with a given Monster object.'''
    super().__init__(monst)
    monst._name = "Poisonous " + monst._name
    monst._hp += 8
        
  def attack(self):
    '''Overrides the attack method of the Monster object and returns the modified behavior with an additional poison-related attack bonus. '''
    return super().attack() + 8