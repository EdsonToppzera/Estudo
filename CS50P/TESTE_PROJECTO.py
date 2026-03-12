#Internation Product Management List
import sys
from deep_translator import GoogleTranslator
from currency_converter import CurrencyConverter
from tabulate import tabulate

def main():
    prints_the_final_list(listing())

###faz a listagem
def listing():

    list_of_list = [{"humano de botas":["i don't know","BRL","50"]},{"rato":["maybe yes","BRL","30"]}]

    return list_of_list

#falta bota o tabulate
###printa a lista
def prints_the_final_list(listafds: list):
    e=0
    for item in listafds:
        e+=1
        for key, value in item.items():
            print(f"""
{e}. {key}
{value[0]}
Price: ${float(value[2]):g} {value[1]}""")

    modifies_the_list(listafds)

###modificação da lista
def modifies_the_list(listafds: list):
    modify_list = input("\nDo you want to modify the list? (yes/no) ")
    if modify_list == "no":
        for item in listafds:
                for key, value in item.items():
                    print(f"[{key}] é [{value[0]}] e vale [{float(value[2]):g}] em [{value[1]}]")
    else:

        modify_or_translate = input("""
+====================================+
|                                    |
> [1] Modify the items               |
|                                    |
> [2] Translate and change currency  |
|                                    |
> [3] Done                           |
|                                    |
+====================================+
Answer: """)

        if modify_or_translate == "1":
            lista_escolhida_dict = choose_item(listafds)
            for key, value in lista_escolhida_dict.items():
                print("Write in the front of what you want to modify")
                nome_modificado = input(f"Name: {key} -> ")
                descrição_modificado = input(f"Description: {value[0]} -> ")
                valor_modificado = input(f"Price: {float(value[2]):g} -> ")
                moeda_modificado = input(f"Currency: {value[1]} -> ")
                lista_dos_bgl_modificado = [nome_modificado,descrição_modificado,moeda_modificado,valor_modificado]
            i = -2
            for var in lista_dos_bgl_modificado:
                i+=1
                if var.strip():
                    if i == -1:
                        muda_key = {}
                        for key, value in lista_escolhida_dict.items():
                            muda_key[key] = var
                        for old, new in muda_key.items():
                            lista_escolhida_dict[new] = lista_escolhida_dict.pop(old)
                    else:
                        for key, value in lista_escolhida_dict.items():
                                value[i] = var

            modifies_the_list(listafds)

        elif modify_or_translate == "2":
            translate_change_currency(listafds)
            print("\nModify again?")
            modifies_the_list(listafds)


        elif modify_or_translate == "3":
            for item in listafds:
                for key, value in item.items():
                    print(f"[{key}] é [{value[0]}] e vale [{float(value[2]):g}] em [{value[1]}]")

        else:
            print("Invalid answer!")
            modifies_the_list(listafds)

###pergunta qual vai ser o item da lista
def choose_item(listafds: list):
    print("\nChoose which item:")
    print("+")
    e = 0
    for item in listafds:
        e+=1
        for key, value in item.items():
            print(f"""|
> [{e}] {key}""")
    print("""|
+""")
    resposta_choose = input("Answer: ")
    return listafds[int(resposta_choose)-1]


#falta testa isso aqui
def translate_change_currency(listafds):
    resposta_tcc = input("""
+====================================+
|                                    |
> [1] Translate                      |
|                                    |
> [2] Change currency                |
|                                    |
> [3] Both                           |
|                                    |
+====================================+
Answer: """)

    if resposta_tcc == "1":
        resposta_qual_lingua = input("What language do you want it to be?(EX:en/pt-br/es) ")

        #muda_key = {}
        #for key, value in lista_escolhida_dict.items():
            #muda_key[key] = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(key)
        #for old, new in muda_key.items():
            #lista_escolhida_dict[new] = lista_escolhida_dict.pop(old)

        for lista in listafds:
            for key, value in lista.items():
                #key = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(key)
                value[0] = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(value[0])
            muda_key = {}
            for key, value in lista.items():
                muda_key[key] = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(key)
            for old, new in muda_key.items():
                lista[new] = lista.pop(old)


    elif resposta_tcc == "2":
        resposta_qual_currency = input("What currency do you want it to be?(EX:USD/BRL/EUR) ")
        c = CurrencyConverter()
        for lista in listafds:
            for key, value in lista.items():
                value[2] = c.convert(value[2], value[1], resposta_qual_currency)
                value[1] = resposta_qual_currency

    elif resposta_tcc == "3":
        resposta_qual_lingua = input("What language do you want it to be?(EX:en/pt-br/es) ")
        for lista in listafds:
            for key, value in lista.items():
                key = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(key)
                value[0] = GoogleTranslator(source='auto', target=resposta_qual_lingua).translate(value[0])

        resposta_qual_currency = input("What currency do you want it to be?(EX:USD/BRL/EUR) ")
        c = CurrencyConverter()
        for lista in listafds:
            for key, value in lista.items():
                value[2] = c.convert(value[2], value[1], resposta_qual_currency)
                value[1] = resposta_qual_currency

    else:
        print("Invalid answer!")
        translate_change_currency(listafds)

    return listafds


if __name__ == "__main__":
    main()
