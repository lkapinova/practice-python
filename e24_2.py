# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

i = [0,1,2]
j = [2,1,2]
k = [1,1,1]
matrix = [i, j, k]

print(matrix)
print(matrix [2][0])

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
    

print(get_row(matrix,0))
print(get_column(matrix,2))
print(get_diagonals(matrix))
