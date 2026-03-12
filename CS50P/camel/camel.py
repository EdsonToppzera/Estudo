def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    snake(camel)

def snake(nome):
    for i in nome:
        if str(i).isupper():
            print("_" + str(i).lower(), end="")
        else:
            print(i, end="")
        continue
main()


