

print("welcome to quiz")
n = input("Enter your name:")

playing = input("Do you want to play ?",)

if playing.lower() != "yes" :
    quit()

print("Let's Play....")

score = 0
answer = input("tumhara khuda kon hai?")
if answer == "allah":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("pehle imam kon hai?")
if answer == "imam ali":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does www stand for?  ")
if answer == "world wide web":
    print("correct")
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " question correct!")
print("you got",str((score/ 3)* 100) + "%")








