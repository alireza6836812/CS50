# TODO
from cs50 import get_float

while True:
    p = get_float("Change owed: ")
    if p > 0:
        break

coins_number = round(p * 100)

number = 0
while coins_number > 0:
    if coins_number >= 25:
        coins_number -= 25
        number += 1
    elif coins_number >= 10:
        coins_number -= 10
        number += 1
    elif coins_number >= 5:
        coins_number -= 5
        number += 1
    else:
        coins_number -= 1
        number += 1

print(number)
