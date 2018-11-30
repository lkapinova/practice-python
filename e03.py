a= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
b=[]

number = input("Enter any number less than 1000: ")
number = int(number)

# for x in list (a):
#     if x<number:
#         b.append(x)

b = [x for x in list (a) if x < number]

print (b)



 
