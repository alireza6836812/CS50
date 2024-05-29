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
    "December"
]

while True:
    input_date = input("Date: ")
    try:
        if "/" in input_date:
            month, day, year = input_date.split("/")
        elif "," in input_date:
            month_day, year = input_date.split(", ")
            month, day = month_day.split(" ")
            month = (months.index(month)) + 1
        if int(month) > 12 or int(day) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(year)}-{int(month):02}-{int(day):02}")
        break
