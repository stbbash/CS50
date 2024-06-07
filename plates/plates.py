def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# CHECK FOR LENGTH OF STRING, IF STRING CONTAINS ONLY ALPHANUMERIC AND IF STRING STARTS WITH TWO LETTERS
def check_str(plate_str):
    for char in plate_str:
        if (len(plate_str) >= 2 and len(plate_str) <= 6):
            if (plate_str[0].isalpha() and plate_str[1].isalpha()):
                if plate_str.isalnum(): return True
    return False

# CHECK THE FORMAT TO MAKE SURE NO LETTER COME AFTER A NUMBER
def check_format(plate_str):
    for char in range(len(plate_str) - 1):
        if plate_str[char].isdigit() and plate_str[char + 1].isalpha(): return True
    return False

# CHECK FOR ZERO AS FIRST DIGIT
def has_zero_as_first_digit(plate_str):
    num = []
    for char in plate_str:
        if char.isdigit():
            num.append(char)
    if not num: return False
    if num[0] == "0": return True
    return False
# CHECK IF ALL REQUIREMENTS ARE MET FOR THE STRING INPUT
def is_valid(plate_str):
    if check_str(plate_str) and not check_format(plate_str) and not has_zero_as_first_digit(plate_str): return True
    return False

main()
