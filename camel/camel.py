name = input("camelCase: ")
new_name = ""
for i in name:
    new_name += i
    if i == i.upper():
        i = i.lower()
        new_name += "_" + i
        new_name = new_name.replace(i.upper(), "")
print(f"snake_case: {new_name}")
