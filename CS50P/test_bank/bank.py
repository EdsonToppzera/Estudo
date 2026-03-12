def main():
    fala = input("Greeting: ")
    print("$"+str(value(fala)))


def value(greeting):
    #divide o hello, do resto
    fala_hello = greeting.split(" ")

    #extrai so a primeira letra
    fala_h = greeting[0]

    if greeting.strip(" ").lower() == "hello":
        return(0)

    elif fala_hello[0].lower() == "hello,":
        return(0)

    elif fala_h.lower() == "h":
        return(20)

    else:
        return(100)

if __name__ == "__main__":
    main()
