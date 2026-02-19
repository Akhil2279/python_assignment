

def find_runner_up():

    n = int(input())

    data = input().split()

    numbers = []

    for value in data:
        numbers.append(int(value))

    unique_numbers = set(numbers)

    unique_list = list(unique_numbers)

    unique_list.sort()

    runner_up = unique_list[-2]

    return runner_up


if __name__ == "__main__":

    result = find_runner_up()

    print(result)
