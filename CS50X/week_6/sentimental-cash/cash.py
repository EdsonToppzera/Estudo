from cs50 import get_float

def main():
    # 1. Prompt for a non-negative amount of change
    while True:
        dollars = get_float("Change owed: ")
        if dollars >= 0:
            break

    # 2. Convert dollars to cents and round to avoid float errors
    cents = int(round(dollars * 100))

    coins = 0

    # 3. Use the largest coins possible (Quarters)
    while cents >= 25:
        cents -= 25
        coins += 1

    # 4. Use Dimes
    while cents >= 10:
        cents -= 10
        coins += 1

    # 5. Use Nickels
    while cents >= 5:
        cents -= 5
        coins += 1

    # 6. Use Pennies
    while cents >= 1:
        cents -= 1
        coins += 1

    # 7. Print total number of coins
    print(coins)

if __name__ == "__main__":
    main()
