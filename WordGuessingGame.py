import random

name = input("Enter your name:")
print("Good Luck",name)

Sports = ['football','cricket','baseball','volleyball','badminton','chess','carrom','fighting']
word = random.choice(Sports)

print("Guess the sports name")
guesses = ''

turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("___")
            failed +=1

    if failed == 0:
        print("congratulation",name)

    guess = input("enter the character:")
    guesses += guess

    if  guess not in word:
        turns -=1
        print("wrong")
        print(turns,"is left")
        if turns == 0:
            print("sorry try again")

