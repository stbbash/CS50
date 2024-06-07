months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# CHECK FOR THE FIRST DATE FORMAT
def check1(str):
    month = str.split("/")[0]
    day = str.split("/")[1]
    year = str.split("/")[2]
    if int(month) > len(months):
        raise ValueError
    if int(day) > 31:
        raise ValueError
    if len(year) != 4:
        raise ValueError
    if int(day) <= 9 and int(month) <= 9:
        print(f"{year}-0{month}-0{day}")
    elif int(day) <= 9:
        print(f"{year}-{month}-0{day}")
    elif int(month) <= 9:
        print(f"{year}-0{month}-{day}")
    else:
        print(f"{year}-{month}-{day}")


# CHECK FOR THE SECOND DATE FORMAT
def check2(str):
    month_input = str.split(" ")[0]
    for index, value in enumerate(months):
        if month_input == value:
            month = index + 1
    day = str.split(" ")[1]
    year = str.split(" ")[2]
    if month_input not in months:
        raise ValueError
    if int(day.strip(",")) > 31 or "," not in day:
        raise ValueError
    if len(year) != 4:
        raise ValueError
    day = int(day.strip(","))
    if day <= 9 and month <= 9:
        print(f"{year}-0{month}-0{day}")
    elif day <= 9:
        print(f"{year}-{month}-0{day}")
    elif month <= 9:
        print(f"{year}-0{month}-{day}")
    else:
        print(f"{year}-{month}-{day}")


while True:
    date = input("Date: ")
    try:
        check1(date)
        break
    except ValueError:
        pass
    except IndexError:
        pass
    try:
        check2(date)
        break
    except ValueError:
        pass
    except IndexError:
        pass
