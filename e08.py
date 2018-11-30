import random
game = ["stone", "paper", "scissors"]


def SPS(game):
    gamer1 = input("Let's play Rock Paper Scissors game. Enter your choice: ")
    gamer2 = random.choice(game)

    if gamer1 == gamer2:
        print("Indecisively.")
        print("Both players choose %s." % gamer1)

    if (gamer1 == game[1] and gamer2 == game[0]) or (gamer1 == game[0] and gamer2 == game[2]) or (gamer1 == game[2] and gamer2 == game[1]):
        print("Congratulations! You win!")
        print("%s beats %s." % (gamer1.capitalize(), gamer2))

    if (gamer1 == game[0] and gamer2 == game[1]) or (gamer1 == game[2] and gamer2 == game[0]) or (gamer1 == game[1] and gamer2 == game[2]):
        print("I'am affraid, you lost.")
        print("%s does not beat %s." % (gamer1.capitalize(), gamer2))


while True:
    SPS(game)
    answer = input("Another game? (y/n): ")
    if answer != "y":
        break

print("Goodbye!")
