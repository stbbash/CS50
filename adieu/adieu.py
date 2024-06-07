names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
if not names or name == "":
    print("")
elif len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    last_name = names.pop()
    result = ", ".join(names)
    print(f"Adieu, adieu, to {result}, and {last_name}")
print("\n")
