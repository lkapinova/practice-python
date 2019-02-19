# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthday_list = {
    "Tom": "27.6.1980",
    "Anicka": "24.9.2013",
    "Terezka": "19.10.2016",
    "Vlada": "21.5.1956",
    "Jaris": "1.4.1958",
    "Tana": "18.1.1954",
    "Mirek": "7.8.1953",
    "Dada": "11.8.1992",
    "Luna": "7.6.1980",
    "Pepi": "10.12.2013",
    "Jana": "16.1.1980",
    "Paja": "29.8.1979",
    "Adam": "24.6.2010",
    "Kaja": "7.10.2011"
}

print("Welcome to the birthday list. It includes the birthdays of:")
for key in birthday_list.keys():
    print(key)

chosen_person = input(
    " Who's birthday do you want to look up? Enter her/his name: ")
print(chosen_person + " was born on " + birthday_list.get(chosen_person) + ".")
