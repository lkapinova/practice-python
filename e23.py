# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

p = []
h = []
overlap = []

with open('e23_prime_numbers.txt', 'r') as prime, open('e23_happy_numbers.txt', 'r') as happy:

    line = prime.readline()
    while line:
        p.append(int(line))
        line = prime.readline()

    line = happy.readline()
    while line:
        h.append(int(line))
        line = happy.readline()

for item in p:
    if item in h:
        overlap.append(item)

print(overlap)
