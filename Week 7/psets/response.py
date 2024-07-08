from validator_collection import checkers


def main():
    if is_valid_email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid_email(email):
    return checkers.is_email(email)


if __name__ == "__main__":
    main()
