while True:
    fraction = input("Fraction: ")
    try:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
        z = round((x / y * 100))
        if x > y:
            raise ValueError
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if z >= 99:
            print("F")
        elif z <= 1:
            print("E")
        else:
            print(f"{z}%")
        break
