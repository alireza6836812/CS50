def main():
    output = fraction("Fraction: ")
    print(output)


def fraction(p):
    while True:
        try:
            x, y = input(p).split("/")
            if 0 <= (int(x)/int(y)) <= 0.1:
                return("E")
            elif 0.9 <= int(x)/int(y) <= 1:
                return("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                return (str(round(int(x)/int(y)*100)) + "%")
        except:
            pass
main()
