# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random
import string

symbols = str('#' '$' '%' '&' '*' ',' '_')


def psw_generator(psw_type):
    
    psw = "undefined yet"
    if psw_type == "weak":
        chars = string.ascii_lowercase
        size = random.randint(4, 6)
        psw = ''.join(random.choice(chars) for x in range(size))

    elif psw_type == "medium":
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        size = random.randint(6, 8)
        psw = ''.join(random.choice(chars) for x in range(size))

    elif psw_type == "strong":
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols
        size = random.randint(8, 12)
        psw = ''.join(random.choice(chars) for x in range(size))

    else:
        print("Invalid input.")

    return psw


psw_type = (input("How strong should be the new password (weak/medium/strong): "))
print((psw_generator(psw_type)))
