from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

if len(sys.argv) > 1:

    if sys.argv[1] in ("-f", "--font"):

        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])

            input = input("Input: ")

            print("Output:"+"\n"+figlet.renderText(input))

        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


elif len(sys.argv) == 1:

    figlet.setFont(font=random.choice(figlet.getFonts()))

    input = input("Input: ")

    print("Output:"+"\n"+figlet.renderText(input))
