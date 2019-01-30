# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

import random

with open('e30.txt') as f:
    words = list(f)

print(random.choice(words).strip())
