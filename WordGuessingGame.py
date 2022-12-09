# Overview

# 1)Build a word guessing game, in which the user selects a word from list.
# 2)Let’s say User selected a character if it's in the list it will move to next character to guess.
# 3)Character will bw choose random from the list by system

# requirement
# random module

import random

Name = input("Enter your name:")
print("Good luck", Name)

words = ['mercedes', 'ferrari', 'ford', 'buggati', 'tata', 'suzuki', 'audi']
word = random.choice(words)

print("Guess the  characters of car")
guesses = ''

turns = 7
while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win", Name)
        print("The word u guess which is", word)
        break

    print()
    guess = input("Guess the character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("You have", + turns, "left")
        if turns == 0:
            print("you loose")

