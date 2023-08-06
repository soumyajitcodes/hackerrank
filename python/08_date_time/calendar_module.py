import calendar

if __name__ == "__main__":
    month, date, year = map(int, input().split())

    print(calendar.day_name[calendar.weekday(year, month, date)].upper())
