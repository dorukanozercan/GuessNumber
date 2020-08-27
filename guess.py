# guess a number game

import random

print("what is your name?")
name = input()
print("Welcome to the guessing number game, " + name.title() + ".")
print("Guess a number, NOW! (You have 3 lives.)")

secretNumber = random.randint(1, 10)

for life in range(1, 4):
    guess = int(input())  # since input returns a string converting it to int
    if guess == secretNumber:
        print("YOU FOUND IT!")
        break  # exit loop
    elif guess > secretNumber:
        print("go lower")
    elif guess < secretNumber:
        print("go higher")

if secretNumber == guess:
    print("It took " + str(life) + " tries to find the number. :)")
else:
    print("Unfortunately you couldn't find the number. Correct number was " + str(secretNumber))

input("press ENTER TO EXIT")

