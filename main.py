# Christopher Soriano and Justin Donate
# 4/18/23
# This program allows the user to create a Monster of their choice. They can add abilities that increase the HP and Attack points of their monster.

import check_input

from alien import Alien
from beast import Beast
from undead import Undead
from fire import Fire
from flying import Flying
from lasers import Lasers
from poison import Poison

def main():
  print("Monster Maker\n")

  print("Choose a base monster:")
  print("1. Alien\n2. Beast\n3. Undead")
  choose_base = check_input.get_int_range("Enter choice: ", 1, 3)

  print("")

  play = True

  if choose_base == 1:
    monster = Alien()
  elif choose_base == 2:
    monster = Beast()
  elif choose_base == 3:
    monster = Undead()

  while play == True:
    print(monster)
    print("Add an ability:\n1. Fire\n2. Flying\n3. Lasers\n4. Poison\n5. Quit")
    add_ability = check_input.get_int_range("", 1, 5)

    if add_ability == 1:
      monster = Fire(monster)
      Fire(monster)
    elif add_ability == 2:
      monster = Flying(monster)
      Flying(monster)
    elif add_ability == 3:
      monster = Lasers(monster)
      Lasers(monster)
    elif add_ability == 4:
      monster = Poison(monster)
      Poison(monster)
    else:
      play = False

    print("")
main()