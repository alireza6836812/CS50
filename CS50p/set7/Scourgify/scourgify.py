import csv
import sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
    sys.exit("Invalid arguments.")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as myinput, open(sys.argv[2], "w", newline="") as myoutput:
        r = csv.DictReader(myinput)
        w = csv.DictWriter(myoutput, fieldnames=["first", "last", "house"])
        w.writeheader()
        for i in r:
            last_name, first_name = i["name"].strip().split(", ")
            w.writerow({"first": first_name, "last": last_name, "house": i["house"]})

except FileNotFoundError:
    sys.exit("File does not exist.")
