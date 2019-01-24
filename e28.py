# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

import random

def max_of_three (a,b,c):
    if a > b and a > c:
        print("The biggest number is %d." % a)
    if b > a and b > c:
        print("The biggest number is %d." % b)
    if c > a and c > b:
        print("The biggest number is %d." % c)
    print("a = %d, b = %d, c = %d" %(a,b,c))

if __name__ == "__main__":

    a = random.randint(1,1000)
    b = random.randint(1,1000)
    c = random.randint(1,1000)
    max_of_three (a,b,c)

    

