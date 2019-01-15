# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

i = [1,1,0]
j = [0,1,2]
k = [1,1,1]
matrix = [i, j, k]

def get_row(matrix,i):
    r = []
    for j in range(len(matrix)):
        r.append(matrix[i][j])
    return r

def get_column(matrix,j):
    c = []
    for i in range(len(matrix)):
        c.append(matrix[i][j])
    return c

def get_diagonals(matrix):
    size = len(matrix)
    d1 = []
    d2 = []
    for i in range(size):
        d1.append(matrix[i][i])
        d2.append(matrix[(size-1-i)][i])
    return d1, d2
    

for i in range (3):
    r = get_row(matrix,i)
    print("r=", r)
    if r[0] == r[1] == r[2] and r[i] != 0:
        print("Winner is player %d." %r[i])

for i in range (3):
    c = get_column(matrix,i)
    print("c=", c)
    if c[0] == c[1] == c[2] and c[i] != 0:
        print("Winner is player %d." %c[i])

d = get_diagonals(matrix)
print("d=", d)
if d[0][0] == d[0][1] == d[0][2] and d[0][0] != 0:
    print("Winner is player %d." %d[0][0])
if d[1][0] == d[1][1] == d[1][2] and d[1][0] != 0:
    print("Winner is player %d." %d[1][1])



