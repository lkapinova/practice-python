# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Input
name=input("Enter your name: ")
age=input("Enter your age: ")
copiesnumber=input("Enter any number from 1 to 10: ")
import datetime
now = datetime.datetime.now()

age=int(age)

#Name and age statement
message1="Your name is %s and you are %d.\n" % (name, age)

print(int(copiesnumber) * message1)

#Year of 100 years birthday
onehundred=100-age+int(now.year)

message2="You will be 100 years old in %d.\n" % (onehundred)
print(int(copiesnumber) * message2)

