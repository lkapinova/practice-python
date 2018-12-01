import random

pc = random.randint(1,9)
player = int(input("Guess the number from 1 to 9: "))

if player == pc:
    print ("Your guess was exactly right!")
if player < pc:
    print("Your guess was too low!")
if player > pc:
    print("Your guess was too high`!")

# print (pc, player)
