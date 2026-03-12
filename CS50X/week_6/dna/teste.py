import csv
import sys

rows = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)

print(rows)
