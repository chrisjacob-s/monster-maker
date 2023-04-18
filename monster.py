# Chris
import abc

class Monster(abc.ABC):
  def __init__(self, name, hp):
    self._name = name
    self._hp = hp

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name

  @property
  def hp(self):
    return self._hp

  @hp.setter
  def hp(self, hp):
    self._hp = hp

  def __str__(self):
    return f"Name: {self._name}\nHP: {self._hp}\nAttack: {self.attack()}"

  @abc.abstractmethod
  def attack(self):
    pass