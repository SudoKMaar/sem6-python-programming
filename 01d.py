date_string = input("Enter a date in YYYY-MM-DD format: ")
year, month, day = map(int, date_string.split('-'))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

if year < 1 or month < 1 or month > 12 or day < 1 or day > month_length:
    print(f"The date {date_string} is not valid.")
else:
    print(f"The date {date_string} is valid.")
    
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print(f"The next date is {year}-{month:02d}-{day:02d}.")