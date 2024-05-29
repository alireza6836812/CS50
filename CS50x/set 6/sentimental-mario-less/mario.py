while True:
    try:
        h = int(input("Height: "))
        if (h >= 1) and (h <= 8):
            break
    except:
        print("", end="")

empty = 1
for j in range(0, h):
    for empty in range(0, h - j - 1):
        print(" ", end="")
    for i in range(0, j + 1):
        print("#", end="")
    print()
