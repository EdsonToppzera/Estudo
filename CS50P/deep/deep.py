pergunta = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
pergunta_top = pergunta.strip(" ").lower()
if pergunta_top == "42" or pergunta_top == "forty-two" or pergunta_top == "forty two":
    print("Yes")
else:
    print("No")
