# Chris
import abc

class Monster(abc.ABC):
  ''' Represents the name and hp of the monster
  Attributes:
    _name (str) = name of monster
    _hp (int) = hp of monster
  '''
  def __init__(self, name, hp):
    self._name = name
    self._hp = hp

  @property
  def name(self):
    ''' Getter for monster name '''
    return self._name

  @name.setter
  def name(self, name):
    ''' Setter for monster name '''
    self._name = name

  @property
  def hp(self):
    ''' Getter for monster hp '''
    return self._hp

  @hp.setter
  def hp(self, hp):
    ''' Setter for monster hp '''
    self._hp = hp

  def __str__(self):
    ''' Returns a string of the monster's name, HP, and attack power '''
    return f"Name: {self._name}\nHP: {self._hp}\nAttack: {self.attack()}"

  @abc.abstractmethod
  def attack(self):
    ''' Abstract method of the monster's attack power '''
    pass