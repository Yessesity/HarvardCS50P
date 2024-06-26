def main():
    date = input("Date: ").strip()
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
    try:
        month, day, year = date.split("/")
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")

    except:
        try:
            month, day, year = date.split(" ")
            if month in month_num:
                print(f"{year}-{month_num[month].zfill(2)}-{day.strip(",").zfill(2)}")
        except:
            main()

main()
