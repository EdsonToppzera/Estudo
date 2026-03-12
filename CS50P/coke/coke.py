def maquina(grana, coke):
    troco = coke - grana
    if grana != 5 and grana != 10 and grana != 25:
        main()
    elif grana > coke:
        print("Change Owed: "+str(abs(troco)))
    elif grana == coke:
        print("Change Owed: 0")
    elif grana < coke:
        print("Amount Due: " + str(troco))
        grana = int(input("Insert Coin: "))
        coke = troco
        maquina(grana, coke)

def main():
    coke = 50
    print("Amount Due: " + str(coke))
    dinheiro = int(input("Insert Coin: "))
    maquina(dinheiro, coke)

main()


