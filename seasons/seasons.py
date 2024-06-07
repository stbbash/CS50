from datetime import datetime, date
import sys
import inflect

def main():
    birthdate_input = input("Enter your date of birth (YYYY-MM-DD): ")
    print(calculate_age_in_minutes(birthdate_input))




def calculate_age_in_minutes(birthdate):
    try:
        birth_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
        current_datetime = datetime.combine(date.today(), datetime.min.time())
        age_in_minutes = round((current_datetime - birth_datetime).total_seconds() / 60)
        change_to_words = inflect.engine()
        age_in_words = change_to_words.number_to_words(age_in_minutes, andword="")
        return f"{age_in_words.capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
