import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    pattern = re.compile(r"\bum\b", re.IGNORECASE)
    matches = pattern.findall(s)

    for match in matches:
        count += 1
    return count

if __name__ == "__main__":
    main()
