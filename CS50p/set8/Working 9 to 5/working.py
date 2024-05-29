import re


def main():
    myinput = input("Hours: ")
    output = convert(myinput)
    print(output)


def convert(s):
    r = re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s)
    if match := r:
        sh, sm, sp, eh, em, ep = match.groups()

        if sm is None and em is None:
            sm = 0
            em = 0
        sh, st_min, eh, em = map(int, [sh, sm, eh, em])

        if sh != 12 and sm == "PM":
            sh += 12
        elif sh == 12 and sp == 'AM':
            sh = 0

        if ep == "PM" and eh != 12:
            eh += 12
        elif ep == "AM" and eh == 12:
            eh = 0

        if not 0 <= sh <= 23:
            raise (ValueError("Invalid arguments"))
        if not 0 <= sm <= 59:
            raise (ValueError("Invalid arguments"))
        if not 0 <= eh <= 23:
            raise (ValueError("Invalid arguments"))
        if not 0 <= em <= 59:
            raise (ValueError("Invalid arguments"))

        return (f"{sh:02d}:{sm:02d} to {eh:02d}:{em:02d}")
    raise (ValueError("Invalid arguments"))


if __name__ == "__main__":
    main()
