# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

counter_dict = {}

with open("e22_1.txt", "r") as open_file:
    line = open_file.readline()

    while line:
        line = line[3:-26]

        if line in counter_dict:
            counter_dict[line] += 1

        else:
            counter_dict[line] = 1

        line = open_file.readline()

print(counter_dict)
