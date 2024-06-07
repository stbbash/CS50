import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguement")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguements")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        before = sys.argv[1]
        after = sys.argv[2]
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            with open(after, "w", newline='') as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    house = row["house"]
                    name = row["name"]
                    name = name.strip()
                    last_name = name.split(", ")[0]
                    first_name = name.split(", ")[1]
                    writer.writerow({"first": first_name, "last": last_name, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {before}")
