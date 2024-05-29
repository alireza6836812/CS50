price = 50
total_paid = 0
coins_list = [25, 10, 5]

while price > 0:
    print(f"Amount Due: {price}")
    pay = int(input("Insert Coin: "))
    if pay in coins_list:
        price = price - pay
        total_paid = total_paid + pay

if total_paid >= price:
    print(f"Change Owed: {total_paid - 50}")