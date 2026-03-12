from cs50 import get_string

def main():
    text = get_string("Text: ")

    letters = 0
    words = 1  # Start at 1 assuming there's at least one word
    sentences = 0

    for char in text:
        # Count letters (A-Z, a-z)
        if char.isalpha():
            letters += 1
        # Count words (sequences separated by spaces)
        elif char.isspace():
            words += 1
        # Count sentences (ending in . ! or ?)
        elif char in [".", "!", "?"]:
            sentences += 1

    # Calculate L and S per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Compute index and round
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Output results based on grade constraints
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()
