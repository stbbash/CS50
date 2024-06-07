import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define regular expression to match valid input formats
    pattern = re.compile(r'^(1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM)$')

    # Check if the input matches the expected format
    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid input format. Please use '9:00 AM to 5:00 PM' or '9 AM to 5 PM'.")

    # Extract hours and meridiem from the input
    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()

    # Convert hours to 24-hour format
    start_hour = int(start_hour) % 12
    end_hour = int(end_hour) % 12

    # Adjust for PM hours
    if start_meridiem == 'PM':
        start_hour += 12
    if end_meridiem == 'PM':
        end_hour += 12

    # Validate the converted hours
    if not (0 <= start_hour <= 23) or not (0 <= end_hour <= 23):
        raise ValueError("Invalid time. Please provide valid hours between 1 and 12.")

    # Format the result in 24-hour format
    result = f"{start_hour:02d}{start_minute if start_minute else ':00'} to {end_hour:02d}{end_minute if end_minute else ':00'}"
    return result

if __name__ == "__main__":
    main()
