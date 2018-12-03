# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html


def Divisors(num):
    list = range(1, num + 1)
    divisors_list = []
    for x in list:
        if num % x == 0:
            divisors_list.append(x)
    if len(divisors_list) == 2:
        print("You find a prime number.")
    return(divisors_list)


num = int(input("Enter any number: "))
divisors = Divisors(num)
print("The number %d can be devided by:" % num, (divisors))
