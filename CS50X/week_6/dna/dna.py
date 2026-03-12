import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Not enough arguments!!!")

    # TODO: Read database file into a variable
    csv_file=sys.argv[1]
    with open(str(csv_file)) as file:
        people = csv.DictReader(file)
        titulos=people.fieldnames

        # print("1titulos: ") #debug
        # print(titulos) #debug
        # print("---") #debug


    # TODO: Read DNA sequence file into a variable
    text_file=sys.argv[2]
    with open(str(text_file), 'r') as f:
        dna = f.read()


    # TODO: Find longest match of each STR in DNA sequence
    values = ["default_name"]
    for i in titulos[1:]:
        values.append(longest_match(dna,i))
    dict_dna = dict(zip(titulos, values))

    # print("2dict_dna: ") #debug
    # print(dict_dna) #debug
    # print("---") #debug

    # TODO: Check database for matching profiles
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        its_over=False
        for person in reader:
            if its_over:
                break
            ok=0
            for (key, value), (key2, value2) in zip(person.items(), dict_dna.items()):
                if key == "name":
                    nome_atual=value
                    continue

                if str(key) == str(key2) and int(value) == int(value2):
                    ok+=1
                    if ok == len(person)-1:
                        print(nome_atual)
                        its_over=True

        if not its_over:
            print("No match")


    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
