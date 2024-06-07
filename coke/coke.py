# Check to accept required cents first
while True:
    print("Amount Due: 50")
    coins = int(input("Insert Coins: "))
    if coins == 25 or coins == 10 or coins == 5:
        break
# Check to see if the ammount is upto 50 cents and return change if any
while coins < 50:
    print(f"Amount Due: {50 - coins}")
    coins += int(input("Insert Coins: "))
    if coins >= 50:
        break
print(f"Change Owed: {coins - 50}")
