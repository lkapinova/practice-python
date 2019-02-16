# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

import random

def random_word():
    with open('e30.txt') as f:
        words = list(f)
    return random.choice(words).strip()

def word_in_dots(word):
    word_lenght = len(word)
    a = "-"
    print(word_lenght*a)
    return word_lenght*a

def letter_placing(a,pos,letter_guess):
    a_as_list = list(a)
    for i in range(0, len(a)):
        if i in pos:
            a_as_list[i] = letter_guess
    print("".join(a_as_list))
    return "".join(a_as_list)

def is_new_game_requested():
    while True:
        new_game = input("Would you like to play again? Enter Y/N: ")
        if new_game == "Y":
            return True
        if new_game == "N":
            return False
        else:
            print ("Incorrect input.")

def play_game():

    word = random_word()
    a = word_in_dots(word)
    used_letters = []
    incorrect_guesses = 0

    while True:
        if a.find('-') != -1:
            letter_guess = input("Try to find a word. Enter a letter that could be a part of it: ")
            pos = []
            if letter_guess in used_letters:
                print("You have already guessed the letter.")
            if letter_guess not in used_letters:
                used_letters.append(letter_guess)   

        for n in range(len(word)):
            if word[n] == letter_guess:
                pos.append(n)

        if pos == []:
            incorrect_guesses += 1

        a = letter_placing(a,pos,letter_guess)
        

        if incorrect_guesses >= 6:
            print("You have lost the game.")
            return
    
        if a.find('-') == -1:
            print("Great! The word is %s." %a)
            return
        

#-----------------------------------------------------------------

if __name__ == "__main__":

    while True:
        play_game()
        if not is_new_game_requested():
            break
    