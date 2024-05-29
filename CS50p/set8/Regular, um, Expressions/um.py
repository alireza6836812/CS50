import re

def main():
    myinput = input("Text: ")
    output = count(myinput)
    print(output)

def count(s):
    r = re.findall(r"\bum\b", s, re.IGNORECASE)
    l = len(r)
    return(l)

if __name__ == "__main__":
    main()
