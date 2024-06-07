import sys
from pyfiglet import Figlet


if len(sys.argv) < 2:
    name = input("Input: ")
    print(name)
    sys.exit()
else:
    if len(sys.argv) > 3:
        sys.exit("Invalid usage")
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    f = Figlet(font=sys.argv[2])
    if not sys.argv[2]:
        sys.exit("Invalid usage")
    name = input("Input: ")
    print(f.renderText(name))

