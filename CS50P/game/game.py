import random
import sys

while True:
    level = input("Level: ")
    if level.isnumeric() == False:
        continue
    if int(level) < 1:
        continue
    else:
        break

fds = int(random.randrange(1,int(level)))

while True:
    guess = input("Guess: ")
    if guess.isnumeric() == False:
        continue
    guess = int(guess)

    if guess < fds:
        print("Too small!")
        continue
    elif guess > fds:
        print("Too large!")
        continue
    elif guess == fds:
        print("Just right!")
        break
