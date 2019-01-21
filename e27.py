# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

# to do: check the input

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#game = [[1,1,1],[2,0,0],[1,1,1]]

print("Please enter the position where your sign should be placed.")
print("The format should be 'row, column'. For first row and third column please enter: 1,3.")


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


if __name__ == "__main__":

    while True:

        place_symbol(1)
        if is_filled(game):
            break
        else:
            place_symbol(2)
            if is_filled(game):
                break

    print(game)
