# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("Enter any number: "))

list = range(1, number+1)
divisors_list = []

for x in list:
    if number % x == 0:
        divisors_list.append(x)

print(divisors_list)
