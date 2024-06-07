foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
amount = 0.00
while True:
    try:
        food_item = input("Item: ").lower()
        for food in foods:
            if food.lower() == food_item:
                price = foods.get(food, None)
                amount += price
                print(f"${amount:.2f}")
    except EOFError:
        break
print("\n")
