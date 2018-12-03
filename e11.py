# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
import time, math

def Divisors(num):
    list = range(1, int(math.sqrt(num + 1)))
    divisors_list = []
    for x in list:
        if num % x == 0:
            divisors_list.append(x)
            divisors_list.append(num/x)
    if len(divisors_list) == 2:
        print("You find a prime number.")
    return(divisors_list)


#num = int(input("Enter any number: "))
num = 40000000
start_time = time.time()
divisors = Divisors(num)
elapsed_time = time.time() - start_time
print("The number %d can be devided by %d divisors: %s" % (num, len(divisors), divisors))
print("Function took %f seconds" % elapsed_time)
