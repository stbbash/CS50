import csv
import sys
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguement")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguements")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        csv_file = sys.argv[1]
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        print(tabulate(data, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("Not a CSV file")
