
import numpy as np

def calculate_determinant():
    N = int(input())
    matrix = []

    for _ in range(N):
        row = list(map(float, input().split()))
        matrix.append(row)
        
    A = np.array(matrix)

    det = np.linalg.det(A)
    return round(det, 2)

if __name__ == '__main__':
    result = calculate_determinant()
    print(result)
