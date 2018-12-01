# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import random

a = 0

while True:
    pc = random.randint(1,9)
    player = input("Guess the number from 1 to 9 (or type exit): ")

    if player.isdigit():
        player = int(player)
        if player == pc:
            print ("Your guess was exactly right!")
        if player < pc:
            print("Your guess was too low!")
        if player > pc:
            print("Your guess was too high!")

    else:
        player = str(player)
        exit="exit"
        if player != exit:
            print ("Invalid input.")
        

    if player == exit:
        print ("Goodby!")
        break
    a += 1
print ("You've played %d times." % a)

# print (pc, player)
