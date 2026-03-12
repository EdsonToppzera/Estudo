import os, sys
from PIL import Image, ImageOps

def main():
    def idk(arg1, arg2):
        image = Image.open(arg1)
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size

        Output = ImageOps.fit(image, shirt_size)
        Output.paste(shirt, shirt)
        Output.save(arg2)

    if len(sys.argv) == 3:
        fds = []
        for infile in sys.argv[1:]:
            f, e = os.path.splitext(infile)
            if e == ".jpg" or e== "jpeg" or e== ".png":
                fds.append(e)
            else:
                sys.exit("Invalid output")

        if fds[0] == fds[1]:
            idk(sys.argv[1],sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")



if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        sys.exit("Input does not exist")
