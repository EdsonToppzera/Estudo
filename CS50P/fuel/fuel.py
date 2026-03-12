def main():

    print(faz_porcentagem("Fraction: "))



def faz_porcentagem(prompt):

    while True:
        try:
        #divide a fração
            prompt = input("Fraction: ")
            intiger = prompt.split("/")
            intiger1 = intiger[0:1]
            intiger2 = intiger[1:2]

        #transforma ela em int
            number = 0
            for digit in intiger1:
                number1 = int(digit)

            for digit in intiger2:
                number2 = int(digit)

        #ve se o denominador é maior
            if number1>number2:
                return faz_porcentagem(prompt)

        #faz a porcentagem
            porcentagem = round((int(number1)/int(number2))*100)

        #decide o output adequado
            if porcentagem <= 1:
                return "E"
            elif porcentagem >= 99:
                return "F"
            else:
                return str(porcentagem)+"%"

    #reseta se da erro

        except ValueError:
            break
        except ZeroDivisionError:
            break


    return faz_porcentagem(prompt)

main()
