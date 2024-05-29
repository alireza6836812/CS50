from tabulate import tabulate
import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Invalid arguments.")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as file:
        output = tabulate(csv.DictReader(file), headers="keys", tablefmt="grid")
        print(output)
except FileNotFoundError:
    sys.exit("File does not exist.")
