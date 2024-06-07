def main():
    question = input("What Is The Time? ").strip()
    answer = convert(question.strip("a.m.").strip("p.m."))
    # check for breakfast
    if answer <= 8 and ("a.m." and "p.m.") not in question:  # check for HR
        print("breakfast time")
    elif answer <= 12 and "a.m." in question:  # check for AM
        print("breakfast time")
    # check for lunch
    elif 8 < answer <= 13 and ("a.m." and "p.m.") not in question:  # check for HR
        print("lunch time")
    elif answer <= 6 and "p.m." in question:   # check for PM
        print("lunch time")
    # check for dinner
    elif 13 < answer <= 19 and ("a.m." and "p.m.") not in question:  # check for HR
        print("dinner time")
    elif 6 < answer < 12 and "p.m." in question:  # check for PM
        print("dinner time")
    else:
        print("")


def convert(time):
    arr = time.split(":")
    hr = int(arr[0]) + (int(arr[1]) / 60)
    return hr


if __name__ == "__main__":
    main()
