

print("welcome to quiz")
n = input("Enter your name:")

playing = input("Do you want to play ?",)

if playing.lower() != "yes" :
    quit()

print("Let's Play....")

score = 0
answer = input("what does cpu stand for? ")
if answer == "central processing unit":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what does ram stand for? ")
if answer == "random access memory":
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








