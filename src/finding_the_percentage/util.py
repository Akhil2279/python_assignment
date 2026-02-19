

def find_average():
    n = int(input())
    student_marks = {}

    for _ in range(n):

        data = input().split()
        name = data[0]
        marks = []

        for value in data[1:]:
            marks.append(float(value))
        student_marks[name] = marks
    query_name = input()
    marks_list = student_marks[query_name]

    total = 0

    for mark in marks_list:
        total = total + mark
    average = total / len(marks_list)

    return average

if __name__ == "__main__":

    result = find_average()

    print(f"{result:.2f}")