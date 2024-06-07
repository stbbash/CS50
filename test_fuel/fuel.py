def main():
    value = input("Fraction: ")
    print(gauge(convert(value)))

def convert(fraction):
    try:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
        if x > y:
            raise ValueError
        z = round((x / y * 100))
        return z
    except ValueError:
        pass
    except ZeroDivisionError:
        raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
