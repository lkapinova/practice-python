# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

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

def add_new_item_json ():
    new_item = input("Would you like to add birthday of another person? Enter 'Y' for yes or 'N' for no: ")
    if new_item == "Y":
        name_inp = input("Enter name: ")
        date_inp = input("Enter the date of birth: ")
        data_inp = {name_inp : date_inp}
        return (data_inp)
    if new_item == "N":
        exit


if __name__ == "__main__":

    with open("birthdays.json", "w") as f:
        json.dump(birthday_list, f)

    data_inp = add_new_item_json()
    #birthdays.append(data_inp)
    print(data_inp)
    dict['birthdays'].append(data_inp)


