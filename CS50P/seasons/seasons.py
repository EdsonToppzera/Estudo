from datetime import date
from datetime import timedelta
import re
import sys
import inflect


def main():
    sang_data = get_minutagem()
    print(sang_data)


class Count:
    def __init__(self, data):
        self.data = data

    #ajeitar isso
    def conta(self):
        if re.search(r"^[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]$", self.data):
            days_difference = (date.today() - date.fromisoformat(self.data)).days
            self.data = days_difference*24*60
        else:
            sys.exit("Invalid date")

    def __str__(self):
        #return fzr minuto vira frase
        #!! e tirar o and
        self.conta()
        return f"{inflect.engine().number_to_words(round(int(self.data))).capitalize().replace(" and","")} minutes"


def get_minutagem():
    data = input("Date of Birth: ")
    return Count(data)


if __name__ == "__main__":
    main()
