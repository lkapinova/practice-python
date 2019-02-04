# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html


def lenght_of_word(word):
    word_lenght = 0
    for i in word:
        word_lenght += 1
    a = "-"
    a = word_lenght*a
    print(a)
    return a


def charposition(word, letter_guess):
    pos = []
    for n in range(len(word)):
        if word[n] == letter_guess:
            pos.append(n)
    print(pos)
    return pos

if __name__ == "__main__":

    # word = "Lenke"
    # lenght_of_word(word)
    # letter_guess = input("Try to find a word. Enter a letter that could be a part of it: ")
    # charposition(word, letter_guess)

    # a = "-----"
    # pos = [1,4]
    # letter_guess = "e"
    # a = a.replace("-", letter_guess,pos[1])
    # print(a)

    a = "-----"
    pos = [1,4]
    # for i in pos:
    #     a = a[:(pos[i])] + 'e' + a[(pos[i]+1):]
    #     print(a)

    a_as_list = list(a)
    for i in range(0, len(a)):
        if i in pos:
            a_as_list[i] = 'e'

    b = "".join(a_as_list)
    print(a)