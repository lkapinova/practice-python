# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

a = [1, 1, 5, 4, 6, 8, 4, 2, 7, 9, 5, 3, 2, 5, 6, 7, 8]


def dupl(a):
    a = set(a)
    a = list(a)
    return(a)


print(dupl(a))
