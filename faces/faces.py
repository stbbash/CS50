def main():
    say = input("What do you want to say? ")

    print(f"{convert(say)}")

def convert(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    if ":(" in str:
        str = str.replace(":(", "🙁")
    return str


if __name__ == "__main__":
    main()

