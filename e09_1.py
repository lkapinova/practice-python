# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Guessing numbers, ends when you find the right number

import random
import sys

pc = random.randint(1, 9)

while True:
    player = input("Guess the number from 1 to 9 (or type 'exit'): ")
    if player.isdigit():
        player = int(player)
        if player < pc:
            print("Your guess was too low! Try it again.")
        if player > pc:
            print("Your guess was too high! Try it again.")
        if player == pc:
            print("Your guess was exactly right!")
            print("Generating a new number.")
            pc = random.randint(1, 9)
    else:
        player = str(player)
        exit = "exit"
        if player == exit:
            break
        if player != exit:
            print("Invalid input.")

print("Goodbye!")
