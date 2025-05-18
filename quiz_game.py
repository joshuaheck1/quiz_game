# Computer Quiz Game... Python mini project
# This is a simple quiz game that tests the user's knowledge of basic computer terminology.
# Built while learning Python! 

print("----- Welcome to the Computer Quiz Game -----")
print()
print("Five questions to test your basic computer knowledge.")
print()


playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print()
    quit()

print("Okay! Let's play :)")
print()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    print()
    score += 1
else:
    print("Incorrect.")
    print()

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    print()
    score += 1
else:
    print("Incorrect.")
    print()

print(" ")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    print()
    score += 1
else:
    print("Incorrect.")
    print()

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    print()
    score += 1
else:
    print("Incorrect.")   
    print()

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print("Correct!")
    print()
    score += 1
else:
    print("Incorrect.")  
    print()

print()
print("You got " + str(score) + " questions correct!")
print("You scored a " + str((score / 5) * 100) + "%.")

print()
print("Thanks for playing the Computer Quiz Game!")
print("Learning Python is fun! :)")
print()
