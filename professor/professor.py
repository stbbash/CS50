import random


def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in range(1, 4):
                break
            raise ValueError
        except ValueError:
            pass
    return n


def generate_integer(level):
    score = 0
    n = 0
    while n < 10:
        answer = None
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        i = 0
        while i < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
            i += 1
            print((f"{x} + {y} = {x + y}"))
        n += 1
    print(score)


if __name__ == "__main__":
    main()
