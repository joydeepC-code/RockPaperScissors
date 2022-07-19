import random
from time import sleep

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
userScore = 0
botScore = 0

print("Welcome to Rock Paper Scissors!")
print("You're up against the computer")
print("This is a 5 round game")
print("Good luck!")

i = 0
while i <= 5:
    userNum = input(
        "Select your weapon: \nEnter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissors \n")
    userChoice = ""

    if userNum == '1':
        userChoice = rock

    elif userNum == '2':
        userChoice = paper

    elif userNum == '3':
        userChoice = scissors

    else:
        print("The weapon doesn't exist, exiting...")
        exit(0)

    botNum = random.randint(1, 3)
    botChoice = ""

    if botNum == 1:
        botChoice = rock

    elif botNum == 2:
        botChoice = paper

    elif botNum == 3:
        botChoice = scissors

    # draw scenario
    if botChoice == userChoice:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("It's a draw! \n")

    # Computer winning scenarios
    elif userChoice == rock and botChoice == paper:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("Computer won! \n")
        botScore += 1

    elif userChoice == paper and botChoice == scissors:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("Computer won! \n")
        botScore += 1

    elif userChoice == scissors and botChoice == rock:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("Computer won! \n")
        botScore += 1

    # user winning scenarios
    elif botChoice == rock and userChoice == paper:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("You won! \n")
        userScore += 1

    elif botChoice == paper and userChoice == scissors:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("You won! \n")
        userScore += 1

    elif botChoice == scissors and userChoice == rock:
        print("\nYour weapon: {}".format(userChoice))
        print("Computer weapon: {} \n".format(botChoice))
        print("Checking result ...\n")
        sleep(2)
        print("You won! \n")
        userScore += 1

    i += 1

sleep(2)
print("Scores: \nYour score: {} \nComputer score: {} \n".format(userScore, botScore))
if userScore > botScore:
    print("You won this game!")
    print("Have a good day!")

elif userScore < botScore:
    print("Computer won this game!")
    print("Have a good day!")

else:
    print("It's a draw!")
    print("Have a good day!")
