import sys

if 3 > len(sys.argv) > 1:
    comando = str(sys.argv[1]).split(".")
    if comando[1] == "py":
        try:

            with open(sys.argv[1], "r") as file:
                contagem = 0
                for line in file:
                    if line.lstrip().startswith("#") == False:
                        if not line.strip() == "":
                            contagem += 1
                print(contagem)


        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
else:
    sys.exit("Too few command-line arguments")
