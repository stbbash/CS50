def main():
    answer = input("Greetings: ")
    print(value(answer))

def value(greeting):
    if "hello" in greeting.lower().strip() and greeting.lower().strip().startswith("h"):
        return 0
    elif greeting.lower().strip().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
