# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html 

number = input("Enter any number: ")
number = int(number)

if (number % 2) == 0:
    print("%d is even/sudé number." % number)

else:
    print("%d is odd/liché number." % number)

# divisibility by 4
if (number % 4) == 0:
    print("%d is divisible by 4." % number)

else:
    print("%d is not divisible by 4." % number)


# devide num and check
num = input("Enter any number to be devide: ")
num = int(num)
check = input("Enter any number to devide by: ")
check = int(check)

if (num % check) == 0:
    print("%d je dělitelné %d." % (num, check))

else:
    print("%d není dělitelné %d." % (num, check))
