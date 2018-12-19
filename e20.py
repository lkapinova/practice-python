# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

a = [1, 3, 5, 30, 42, 43, 500]


def element_search(b):

    while True:
        if b == "exit":
            break

        if b in list(a):
            print("The number is in the list")
            break
        if b not in list(a):
            print("The number is not in the list.")
            break


b = int(input("Enter a number from 0 to 500: "))

element_search(b)
