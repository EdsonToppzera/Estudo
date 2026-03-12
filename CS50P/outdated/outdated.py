def main():
    meses = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    #enumera cada mes
    meses_numero = list(enumerate(meses, 1))

    data = input("Date: ")

    def data_sla(sla):

        meses = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

        #enumera cada mes
        meses_numero = list(enumerate(meses, 1))

        #verifica q tipo de data foi inputado
        if "/" in sla:
            data2 = sla.split("/")

            mes = str(data2[0]).strip(" ")

            ano = str(data2[2]).strip(" ")

            if mes.isnumeric() == True:
                if int(mes) < 13:
                    mes_printado = f"{int(mes):02}"
                    dia = int(data2[1])
                    if dia < 32:
                        dia_printado = f"{dia:02}"

                        print(f"{ano}-{mes_printado}-{dia_printado}")
                    else:
                        main()

                else:
                    main()

            else:
                main()


        elif " " in sla:
            if "," in data:
                data2 = sla.replace(",","").split(" ")

                mes = str(data2[0])
                if mes in meses:

                    dia = int(data2[1])
                    if dia < 32:

                        dia_printado = f"{dia:02}"


                        #printa o modo certo da data inputada
                            #tem q descubri como acha o mes em meses_numero

                        for numero, meses in meses_numero:
                            if meses == mes:

                                mes_printado = f"{int(numero):02}"

                                print(f"{data2[2]}-{mes_printado}-{dia_printado}")
                    else:
                        main()

                else:
                    main()

            else:
                main()

    data_sla(data)

main()

