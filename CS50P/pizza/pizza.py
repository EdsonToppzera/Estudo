import sys
import csv
from tabulate import tabulate

if 3 > len(sys.argv) > 1:
    comando = str(sys.argv[1]).split(".")
    if comando[1] == "csv":
        try:
            tabela = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for pizza, small, large in reader:
                    tabela.append({"pizza": pizza, "small": small, "large": large})

            table = []
            for coisas in tabela:
                table.append([coisas["pizza"], coisas["small"], coisas["large"]])

            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
else:
    sys.exit("Too few command-line arguments")
