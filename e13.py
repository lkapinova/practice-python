# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def fibonacci(num):
    num = int(num)
    num1 = 1
    fibonacci_sequence = []
    a, b = 0, 1

    while num1 <= num:
        fibonacci_sequence.append(a+b)

        num1 += 1
        a, b = b, a+b

    else:
        return (fibonacci_sequence)


num = input("How many Fibonnaci numbers would you like to see: ")

output = fibonacci(num)
print(output)
