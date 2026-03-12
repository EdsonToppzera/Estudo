import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif 4 > len(sys.argv) > 1:
    students = []
    try:

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name":row["name"], "house": row["house"]})

        listafds = []

        for info in students:
            full_names = info["name"].split(",")
            first = full_names[1].strip()
            last = full_names[0]
            house = info["house"]
            listafds.append({'first': first, "last": last, "house": house})
            with open(sys.argv[2], "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                writer.writerows(listafds)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
