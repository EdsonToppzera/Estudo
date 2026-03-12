fala = input("Greeting: ").lower()

#divide o hello, do resto
fala_hello = fala.split(" ")

#extrai so a primeira letra
fala_h = fala[0]

if fala.strip(" ") == "hello":
    print("$0")

elif fala_hello[0] == "hello,":
    print("$0")

elif fala_h == "h":
    print("$20")

else:
    print("$100")
