# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html


def txt_to_list(txt_file):
    list = []
    with open(txt_file) as f:

        line = f.readline()
        while line:
            list.append(int(line))
            line = f.readline()

    return list


if __name__ == "__main__":

    p = txt_to_list('e23_prime_numbers.txt')
    h = txt_to_list('e23_happy_numbers.txt')
    overlap = []

    for item in p:
        if item in h:
            overlap.append(item)

    print(overlap)
