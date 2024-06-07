import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass
option = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < option:
            print("Too small!")
        elif guess > option:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
