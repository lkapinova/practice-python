# https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

from bokeh.plotting import figure, show, output_file
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

a = dict(Counter(months))

output_file("e36_plot.html")

x_categories = list(num_to_string.values())
x = list(a.keys())
y = list(a.values())

p = figure(x_range=x_categories, plot_width=700, plot_height=400)
p.vbar(x=x, top=y, width=0.5)

show(p)