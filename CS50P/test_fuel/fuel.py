def main():
    fraction = input("Fraction: ")
    fraction_real = convert(fraction)
    print(fraction_real)
    print(gauge(fraction_real))

def convert(fraction):
    try:
        #divide a fração

        intiger = fraction.split("/")
        intiger1 = intiger[0:1]
        intiger2 = intiger[1:2]

        #transforma ela em int
        number = 0
        for digit in intiger1:
            number1 = number*10 + int(digit)

        for digit in intiger2:
            number2 = number*10 + int(digit)

        #ve se o denominador é maior
        if number2 == 0:
            raise ZeroDivisionError
        elif number1>number2:
            raise ValueError

        #faz a porcentagem
        porcentagem = round((int(number1)/int(number2))*100)
        return porcentagem

        #decide o output adequado


    #reseta se da erro

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()
