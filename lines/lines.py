import sys

count = 0
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python File")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line == "" or line == " ":
                continue
            count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
