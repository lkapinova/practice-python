# https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

def gameboard(size):

    size = size.split('x')
    x = int(size[0])

    a = ' ---'
    b = '|   '

    #pylint: disable=unused-variable
    for i in range (1,x+1):
        print(a*x)
        print(b*(x+1))

    print(a * x)
#----------------------------------------------------------------------
def get_row(matrix,i):
    r = []
    for j in range(len(matrix)):
        r.append(matrix[i][j])
    return r
#----------------------------------------------------------------------
def get_column(matrix,j):
    c = []
    for i in range(len(matrix)):
        c.append(matrix[i][j])
    return c
#----------------------------------------------------------------------
def get_diagonals(matrix):
    size = len(matrix)
    d1 = []
    d2 = []
    for i in range(size):
        d1.append(matrix[i][i])
        d2.append(matrix[(size-1-i)][i])
    return d1, d2
#----------------------------------------------------------------------
def place_symbol(p):
    player_input = input("Please enter the coordinates of your symbol: ")
    coord = player_input.split(',')
    r = int(coord[0])-1
    c = int(coord[1])-1

    if game[r][c] == 0:
        game[r][c] = p
    else:
        print("This position's been already filled.")

    return(game)
#----------------------------------------------------------------------
def is_filled(game):
    a = 0
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j] != 0:
                a += 1
    if a == 9:
        return True
    else:
        return False
#----------------------------------------------------------------------


if __name__ == "__main__":

    print("Welcome in TicTacToe game.")
    print("We will start on 3x3 size gameboard.")

    gameboard("3x3")

    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while True:

        place_symbol(1)
        if is_filled(game):
            break
        else:
            place_symbol(2)
            if is_filled(game):
                break

    print(game)

for i in range (3):
    r = get_row(game,i)
    print("r=", r)
    if r[0] == r[1] == r[2] and r[i] != 0:
        print("Winner is player %d." %r[i])

for i in range (3):
    c = get_column(game,i)
    print("c=", c)
    if c[0] == c[1] == c[2] and c[i] != 0:
        print("Winner is player %d." %c[i])

d = get_diagonals(game)
print("d=", d)
if d[0][0] == d[0][1] == d[0][2] and d[0][0] != 0:
    print("Winner is player %d." %d[0][0])
if d[1][0] == d[1][1] == d[1][2] and d[1][0] != 0:
    print("Winner is player %d." %d[1][1])


