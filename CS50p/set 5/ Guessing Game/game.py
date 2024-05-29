import random

while True:
    try:
        number = input("Level: ")
        number = int(number)
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        pass

rand_number = random.randint(1, number)
while True:
    try:
        guess = input("Guess: ")
        guess = int(guess)
        if guess < rand_number:
            print("Too small!")
        elif guess > rand_number:
            print("Too large!")
        else:
            print("Just right")
            break
    except ValueError:
        pass
