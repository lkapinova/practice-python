#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random
a = random.sample(range(1, 100), 30)
b = random.sample(range(1, 100), 20)

ab = [x for x in set(a) if x in b]
result = [x for x in ab if ab.count(x) == 1]

print(a)
print(b)
print(result)