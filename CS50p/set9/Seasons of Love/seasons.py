from datetime import date
import inflect
import sys

def total(birth, today):
    output = (today - birth).days * 24 * 60
    return(output)

def main():
    try:
        myinput = input("Date of Birth: ")
        birth = date.fromisoformat(myinput)
    except ValueError:
        sys.exit("Invalid input.")

    minutes = total(birth, date.today())
    a = inflect.engine()
    print(f"{a.number_to_words(minutes, andword='').capitalize()} {a.plural('minute', minutes)}")

if __name__ == "__main__":
    main()
