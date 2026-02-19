
import calendar

def find_day(month, day, year):

    day_number = calendar.weekday(year, month, day)

    if day_number == 0:
        return "MONDAY"
    elif day_number == 1:
        return "TUESDAY"
    elif day_number == 2:
        return "WEDNESDAY"
    elif day_number == 3:
        return "THURSDAY"
    elif day_number == 4:
        return "FRIDAY"
    elif day_number == 5:
        return "SATURDAY"
    else:
        return "SUNDAY"


if __name__ == "__main__":

    data = input().split()

    month = int(data[0])
    day = int(data[1])
    year = int(data[2])

    result = find_day(month, day, year)

    print(result)
