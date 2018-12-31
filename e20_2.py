# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html


import random


def random_ordered_list(list):
    list = random.sample(range(1, 1000), 50)
    return(sorted(list))


def find(list, number):

    start = 0
    end = len(list)
    middle = int((end-start)/2)

    while True:

        middle_number = list[middle]

        if number == middle_number:
            return True

        elif start+1 == end and start != number and end != number:
            return False

        elif number < middle_number:
            end = middle
            middle = int(end-((end-start)/2))

        elif number > middle_number:
            start = middle
            middle = int(start + (end-start)/2)

        else:
            return False


if __name__ == "__main__":

    number = int(input("Enter a number from 1 to 1000: "))

    list = random_ordered_list(list)
    print(list)

    print(find(list, number))
