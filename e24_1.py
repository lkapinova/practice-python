# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

def gameboard(size):

    size = size.split('x')
    x = int(size[0])

    a = ' ---'
    b = '|   '

    for i in range (1,x+1):
        print(a*x)
        print(b*(x+1))

    print(a * x)

if __name__ == "__main__": 

    gameboard("19x19")
