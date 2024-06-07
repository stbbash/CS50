answer = input("Greetings: ").lower().strip()

if answer.startswith("h") and "hello" in answer:
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
