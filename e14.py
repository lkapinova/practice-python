a = [1, 1, 5, 4, 6, 8, 4, 2, 7, 9, 5, 3, 2, 5, 6, 7, 8]

# print(a)
# a = set(a)
# print (a)

def dupl(a):
    b = []
    for element in a:
        if element not in b:
            b.append(element)
    return b

print(dupl(a))
