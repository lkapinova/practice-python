# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []

import random
a = random.sample(range(1, 100), 20)
b = random.sample(range(1, 100), 20)
c = []

print(a)
print(b)

for item in a:
    if item in b:
        if item not in c:
            c.append(item)

print(c)
