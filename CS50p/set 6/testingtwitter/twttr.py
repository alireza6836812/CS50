def main():
    myinput = input("Input: ")
    output = shorten(myinput)
    print("Output:", output)


def shorten(input_word):
    return "".join([ch for ch in input_word if ch.lower() not in "aeiou"])


if __name__ == "__main__":
    main()
