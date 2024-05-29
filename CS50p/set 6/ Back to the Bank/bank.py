def main():
    myinput = input("Greeting: ")
    print(f"${value(myinput)}")


def value(greeting):
    greeting = greeting.strip()
    greeting = greeting.lower()
    a = greeting.startswith("hello")
    b = greeting.startswith("h")
    if a:
        return 0
    elif b:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
