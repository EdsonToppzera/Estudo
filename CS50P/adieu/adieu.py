import inflect

lista = []
while True:
    try:
        nome = input("Name: ")
        lista.append(nome)

    except EOFError:
            break

lista_real = inflect.engine().join((lista))

print("\n"+"Adieu, adieu, to "+lista_real)
