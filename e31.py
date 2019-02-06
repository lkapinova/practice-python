# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html


def word_in_dots(word):
    # word_lenght = 0
    # for i in word:
    #     word_lenght += 1
    word_lenght = len(word)
    a = "-"
    print(word_lenght*a)
    return word_lenght*a

def letter_position(word, letter_guess):
    pos = []
    for n in range(len(word)):
        if word[n] == letter_guess:
            pos.append(n)
    return pos

def letter_placing(a,pos):
    a_as_list = list(a)
    for i in range(0, len(a)):
        if i in pos:
            a_as_list[i] = letter_guess
    print("".join(a_as_list))
    return "".join(a_as_list)

#-----------------------------------------------------------------

if __name__ == "__main__":

    word = "cenichac"
    a = word_in_dots(word)
    used_letters = []

    while True:
        if a.find('-') != -1:
            letter_guess = input("Try to find a word. Enter a letter that could be a part of it: ")
            if letter_guess in used_letters:
                print("You have already guessed the letter.")
            if letter_guess not in used_letters:
                used_letters.append(letter_guess)

        pos = letter_position(word, letter_guess)
        a = letter_placing(a,pos)
    
        if a.find('-') == -1:
            break
    
    print("Great! The word is %s." %a)