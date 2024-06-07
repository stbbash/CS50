def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# CHECK FOR LENGTH OF STRING, IF STRING CONTAINS ONLY ALPHANUMERIC AND IF STRING STARTS WITH TWO LETTERS
def check_str(str):
    for char in str:
        if (len(str) >= 2 and len(str) <= 6):
            if (str[0].isalpha() and str[1].isalpha()):
                if str.isalnum(): return True
    return False

# CHECK THE FORMAT TO MAKE SURE NO LETTER COME AFTER A NUMBER
def check_format(str):
    for char in range(len(str) - 1):
        if str[char].isdigit() and str[char + 1].isalpha(): return True
    return False

# CHECK FOR ZERO AS FIRST DIGIT
def has_zero_as_first_digit(str):
    num = []
    for char in str:
        if char.isdigit():
            num.append(char)
    if not num: return False
    if num[0] == "0": return True
    return False
# CHECK IF ALL REQUIREMENTS ARE MET FOR THE STRING INPUT
def is_valid(str):
    if check_str(str) and not check_format(str) and not has_zero_as_first_digit(str): return True
    return False

if __name__ == "__main__":
    main()
