# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random


def cowsandbullsgame(number, guess):
    cows = 0
    bulls = 0

    for i in range(len(number)):
        if guess[i] == number[i]:
            cows += 1
        elif guess[i] in number:
            bulls += 1

    return(cows, bulls)


if __name__ == "__main__":
    print("Welcome to the Cows and Bulls game!")
    number = str(random.randint(1000, 9999))
    guesses = 0

    while True:
        guess = str(input("Enter a four digit number: "))

        if guess == "exit":
            break

        cows, bulls = cowsandbullsgame(number, guess)
        guesses += 1

        if cows < 4:
            print("You have %d cows and %d bulls." % (cows, bulls))
        if cows == 4:
            print("You win the game after %d guesses." % guesses)
            print("The right number was %s." % number)
            break
        else:
            print("Your guess was not right. Try it again.")
