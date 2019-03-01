# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

import json
from collections import Counter

with open('e34_birthdays.json', 'r') as f:
    birthdays = json.load(f)

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []

for name, birthday_string in birthdays.items():
    month = int(birthday_string.split(".")[1])
    months.append(num_to_string[month])

print(Counter(months))
