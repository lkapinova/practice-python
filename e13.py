# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibonacci(num):
    num = int(num)
    num1 = 1
    fibonacci_sequence = []
    a = 0
    b = 1

    while num1 <= num:
        c = a+b
        fibonacci_sequence.append(c)

        num1 += 1
        a = b
        b = c

    else:
        return (fibonacci_sequence)

    
num = input("How many Fibonnaci numbers would you like to see: ")

output = fibonacci(num)
print (output)




