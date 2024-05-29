def main():
    myinput = input("Fraction: ")
    myinput = convert(myinput)
    myinput = gauge(myinput)
    print(myinput)


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise (ZeroDivisionError)
            elif x > y:
                raise (ValueError)
            z = round(x / y * 100)
            return (z)
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
