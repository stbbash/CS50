def main():
    str = input("Input: ")
    print(shorten(str))


def shorten(word):
    for line in word:
        if line.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(line, "")
    return f"{word}"

if __name__ == "__main__":
    main()
