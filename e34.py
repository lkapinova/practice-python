# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

birthday_list = {}

with open('e34_birthdays.json', 'r') as f:
    birthday_list = json.load(f)


def add_new_entry():
    name = input("Enter name: ").title()
    date = input("Enter the date of birth: ").format(name)
    birthday_list[name] = date

    with open('e34_birthdays.json', 'w') as f:
        json.dump(birthday_list, f)

    print('{} was added to my birthday list.\n'.format(name))


def find_date():
    name = input("Enter name: ").title()

    try:
        if birthday_list[name]:
            print('{} is born on {}\n'.format(name, birthday_list[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))


def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday_list:
        print(key.ljust(7), ':', birthday_list[key])
    print()

# ___________________________________________________________________________________________________________


if __name__ == "__main__":

    while True:
        what_next = input(
            "What do you want to do? You can Add, Find, List and Quit:\n").capitalize()

        if what_next == "Add":
            add_new_entry()
        elif what_next == "Find":
            find_date()
        elif what_next == "List":
            list_entries()
        elif what_next == "Quit":
            print("Good bye!")
            break
        else:
            print("Incorrect input. Try it again.")
