def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if l < 2 or l > 6:
        return False
    if not all(ch.isalnum() for i in s):
        return False

    a = False
    for i in s:
        if i.isdigit():
            a = True
        if i.isalpha() and a:
            return False

    for i in s:
        if i.isdigit():
            return i != "0"

    return True


if __name__ == "__main__":
    main()
