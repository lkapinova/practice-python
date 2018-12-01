# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in a:
    for y in b:
        if x == y:
            c.append(x)


# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in c:
        if num not in final_list:
            final_list.append(num)
    return final_list


print(Remove(c))
