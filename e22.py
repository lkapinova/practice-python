# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

num_lines = 0

with open("e22.txt", "r") as open_file:
    for line in open_file:
        num_lines += 1
        print("[%03d] %s" % (num_lines, line), end="")

print("Number of lines: %d" % num_lines)
