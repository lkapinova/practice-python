# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

# to do: random list, ordered list, not changing list lenght

import random

def find(list, number):


    while True:
        start = 0
        end = len(list)

        middle = int((end-start)/2)
        middle_number = list[middle]

        if number == middle_number:
            return True
        
        elif len(list) == 2 and list[0] != number and list[1] != number:
            return False
        
        elif number < middle_number:
            list = list[:-middle]
        
        elif number > middle_number:
            list = list[middle:]      
        
        else:
            return False

if __name__ == "__main__":
    #list = random.sample(range(1, 100), 30)
    list = [5, 7, 22, 23, 24, 40, 42, 58, 67, 126, 140, 158, 166, 169, 174, 193, 195, 205, 207, 213, 221, 241, 250, 255, 269, 270, 285, 285, 304, 319, 323, 330, 345, 350, 352, 354, 354, 364, 364, 374, 380, 397, 419, 431, 456, 458, 466, 479, 484, 504,
        506, 511, 518, 519, 549, 557, 560, 577, 589, 596, 620, 621, 627, 628, 632, 636, 642, 648, 648, 652, 663, 665, 665, 672, 677, 687, 696, 698, 724, 737, 800, 826, 841, 865, 869, 869, 878, 891, 897, 900, 930, 939, 946, 957, 969, 979, 991, 992, 994, 999]
    number = int(input("Enter a number from 1 to 1000: "))

    print(find(list, number))
    
        


