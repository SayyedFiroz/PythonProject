# overview

# 1)Build a Number guessing game, in which the user selects a range.
# 2)Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# 3)Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

# requirements
# module :random,math
# formula: Minimum number of guessing = log2(Upper bound – lower bound + 1)

import random as rd
import math as mt

lr = int(input("Enter the lower range:"))
ur = int(input("Enter the upper range:"))

x = rd.randint(lr, ur)
print("\n\tYou 've only ", round(mt.log(ur - lr + 1, 2)), "chances to guess the integer!\n")

count = 0
while count < mt.log(ur - lr + 1, 2):
    count += 1

    guess = int(input("Enter the number to guess:"))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("you guessed to high")

if count > mt.log(ur - lr + 1, 2):
    print("\nThe number is %d" % x)
    print("\t Better luck Try Next Time")
