

from util import find_day

if __name__ == "__main__":

    data = input().split()

    month = int(data[0])
    day = int(data[1])
    year = int(data[2])

    result = find_day(month, day, year)

    print(result)