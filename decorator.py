import monster
import abc

class Decorator(monster.Monster, abc.ABC):
  ''' A decorator that enhances the behavior of a given monster'''
  def __init__(self, monst):
    ''' Initializes a new Decorator object with a given Monster object.'''
    super().__init__(monst.name, monst.hp)
    self._monster = monst
        
  def attack(self):
    '''Overrides the attack method of the Monster object and returns the modified behavior.'''
    return self._monster.attack()