# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

play = input("Welcome on guessing game! Would you like to play? Enter 'y'for yes or 'n' for no: ")
if play == "n":
    exit
input("Please choose one number from 0 to 100. I will try to guess your choice. Have you already chosen one? Type 'y' for yes: ")

def find_number():

    round_counter = 0
    min = 0
    max = 100
    pc_guess = (max - min)/2

    while True:
    
        player_answer = str(input("Is your number %d? Enter 'y' if yes, enter 'l' if your number is lower and 'h' if the number is higher: " % pc_guess))

        if player_answer == "y":
            print("I have find the number in %d rounds." % round_counter)
            break

        if player_answer == "h":
            min = pc_guess
            pc_guess = int(min + (max - min)/2)
            round_counter += 1
    
        if player_answer == "l":
            max = pc_guess
            pc_guess = int(max - (max-min)/2)
            round_counter += 1
    
        if player_answer == "exit":
            break

if __name__ == "__main__":

    find_number()

    