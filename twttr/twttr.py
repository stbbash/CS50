str = input("Input: ")
for line in str:
    if line.lower() in ["a", "e", "i", "o", "u"]:
        str = str.replace(line, "")
print(f"Output: {str}")
