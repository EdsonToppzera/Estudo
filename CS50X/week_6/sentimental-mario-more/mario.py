from cs50 import get_int

def main():
    # 1. Get height from user (between 1 and 8 inclusive)
    while True:
        height = get_int("Height: ")
        if 1 <= height <= 8:
            break

    # 2. Build the pyramids
    for i in range(1, height + 1):
        # Calculate parts of the row
        spaces = " " * (height - i)
        hashes = "#" * i
        gap = "  "

        # Print the row (no trailing spaces after the second hashes)
        print(f"{spaces}{hashes}{gap}{hashes}")

if __name__ == "__main__":
    main()
