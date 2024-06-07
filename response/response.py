import validators

email = input("What is your E-mail address? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")

