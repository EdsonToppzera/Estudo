import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}:?[0-9]{1,2}?|[0-9]) (AM|PM) to ([0-9]{1,2}:?[0-9]{1,2}?|[0-9]) (PM|AM)$",s):

        if int(matches.group(1).split(":")[0])> 12:
            raise(ValueError)
        if int(matches.group(3).split(":")[0]) > 12:
            raise(ValueError)

        #Soma 12 se for PM e separa se tiver minuto
        if matches.group(2) == "AM":
            first = matches.group(1)
        elif matches.group(2) == "PM":
            if ":" in matches.group(1):
                first = str(int(matches.group(1).split(":")[0])+12)+":"+matches.group(1).split(":")[1]
            else:
                first = str(int(matches.group(1))+12)

        if matches.group(4) == "PM":
            if ":" in matches.group(3):
                second = str(int(matches.group(3).split(":")[0])+12)+":"+matches.group(3).split(":")[1]
            else:
                second = str(int(matches.group(3))+12)
        else:
            second = matches.group(3)

        #bota 00 se o input nn tiver
        if ":" not in first:
            first = str(first)+":00"
        if ":" not in second:
            second = str(second)+":00"

        first,first2 = first.split(":")
        second,second2 = second.split(":")
        first = int(first)
        second = int(second)

        if int(first2)> 59:
            raise(ValueError)
        if int(second2) > 59:
            raise(ValueError)

        if matches.group(2) == "AM":
            if first == 12:
                first = 0

        if matches.group(4) == "PM":
            if second == 24:
                second = 12

    else:
        raise(ValueError)

    return(f"{first:02}:{first2} to {second:02}:{second2}")

if __name__ == "__main__":
    main()
