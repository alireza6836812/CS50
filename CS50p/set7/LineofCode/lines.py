import sys

if len(sys.argv) != 2:
    sys.exit("Invalid arguments.")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as file:
        mysum = sum(1 for line in file if line.strip() and not line.lstrip().startswith("#"))
        print(mysum)
except FileNotFoundError:
    sys.exit("File does not exist.")
