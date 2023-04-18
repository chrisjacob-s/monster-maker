# Christopher Soriano and Justin Donate
# 4/18/23
# This program allows the user to create a Monster of their choice. They can add abilities that increase the HP and Attack points of their monster.

import check_input

from alien import Alien
from beast import Beast
from undead import Undead


def main():
  print("Monster Maker\n")

  print("Choose a base monster:")
  print("1. Alien\n2. Beast\n3. Undead")
  choose_base = check_input.get_int_range("Enter choice: ", 1, 3)

  print("")

  if choose_base == 1:
    a = Alien()
    print(a)
    print("Add an ability:")

  elif choose_base == 2:
    b = Beast()
    print(b)
    print("Add an ability:")

  elif choose_base == 3:
    u = Undead()
    print(u)
    print("Add an ability:")


main()