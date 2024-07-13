from datetime import date
import inflect
import sys

p = inflect.engine()


class Date:
    def __init__(self, date_obj):
        self.date = date_obj
        self.today = date.today()

    def convert_minutes(self):
        return round((self.today - self.date).total_seconds()/60)

    def minutes_to_words(minutes):
        return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"

    @classmethod
    def get(cls, inp):
        try:
            date_obj = date.fromisoformat(input(inp))
            return cls(date_obj)
        except ValueError:
            sys.exit("Invalid date")


def main():
    birthday = Date.get("Date of birth: ")
    minutes = birthday.convert_minutes()
    print(Date.minutes_to_words(minutes))


if __name__ == "__main__":
    main()
