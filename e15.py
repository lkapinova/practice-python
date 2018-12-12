# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

string = str(input("Write here a long string: "))
print(string)


def Reverse_str(string):
    string = string.split(" ")
    rev_str = string[-1::-1]
    return rev_str


print(" ".join(Reverse_str(string)))
