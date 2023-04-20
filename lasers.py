import decorator

class Lasers(decorator.Decorator):
  ''' A decorator that adds laser-related properties to a given monster.'''
  def __init__(self, monst):
    '''Initializes a new Lasers object with a given Monster object.'''
    super().__init__(monst)
    monst._name += " with Lasers"
    monst._hp += 2
        
  def attack(self):
    '''Overrides the attack method of the Monster object and returns the modified behavior with an additional laser-related attack bonus.'''
    return super().attack() + 15