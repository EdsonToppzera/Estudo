def main():
    palavra = input("input: ")
    print(shorten(palavra))


def shorten(word):
    for vogal in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        if vogal in word:
            word = word.replace(vogal, "")
    return word



if __name__ == "__main__":
    main()
