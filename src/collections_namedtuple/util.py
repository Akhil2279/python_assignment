
from collections import namedtuple

def calculate_average():

    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    total_marks = 0

    for i in range(n):
        data = input().split()
        student = Student(*data)
        total_marks += int(student.MARKS)

    average = total_marks / n

    print(f"{average:.2f}")

if __name__ == "__main__":
    calculate_average()
    
