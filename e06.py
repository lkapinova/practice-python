string = input("Enter any word/string: ")

string = str(string)
rev_string = string[::-1]

if string == rev_string:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")

print(string, rev_string)
