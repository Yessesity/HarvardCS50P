def main():
    month_num = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
                if is_valid(date):
                    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                    break
                else:
                    pass
            elif "," in date:
                month, day, year = date.split(" ")
                if is_valid(date):
                    print(f"{year}-{month_num[month].zfill(2)}-{day.strip(",").zfill(2)}")
                    break
                else:
                    pass
        except:
            pass

def is_valid(d):
    if "/" in d:
        month, day, year = d.split("/")
        if int(month) <= 12 and int(day) <= 31 and month.isnumeric():
            return True
    elif "," in d:
        month, day, year = d.split(" ")
        if int(day.strip(",")) <= 31 and day.strip(",").isnumeric():
            return True

main()