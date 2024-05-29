import inflect

text = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: ").strip())
    except EOFError:
        print()
        break
text = text.join(names)
print(f"Adieu, adieu, to {text}")
