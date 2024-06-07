question = input("Expression: ").strip()
ans = question.split()
x = int(ans[0])
y = ans[1]
z = int(ans[2])
if y == "+":
    answer = float(x + z)
    print(f"{answer:.1f}")
elif y == "-":
    answer = float(x - z)
    print(f"{answer:.1f}")
elif y == "*":
    answer = float(x * z)
    print(f"{answer:.1f}")
elif y == "/":
    answer = float(x / z)
    print(f"{answer:.1f}")
else:
    print("Not Valid")
