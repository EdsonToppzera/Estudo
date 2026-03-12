expressão = input("Expression: ").split(" ")

x = expressão[0]
y = expressão[1]
z = expressão[2]

resposta = x + y + z

amigo = eval(resposta)

print(float(amigo))
