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
        if int(month) <= 12 and int(day) <= 31 and month.isnumeric():
            print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        else:
            main()
    except:
        try:
            if "," in date:
                month, day, year = date.split(" ")
                if month in month_num and int(day.strip(",")) <= 31 and day.strip(",").isnumeric():
                    print(f"{year}-{month_num[month].zfill(2)}-{day.strip(",").zfill(2)}")
                else:
                    main()
            else:
                main()
        except:
            main()

main()
