my_list = []
grocery = {}
while True:
    try:
        food_item = input().upper()
        my_list.append(food_item)
        my_list.sort()
    except EOFError:
        break
for food in my_list:
    grocery[food] = grocery.get(food, 0) + 1
for food, count in grocery.items():
    print(count, food)
