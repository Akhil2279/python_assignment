
import numpy as np

def calculate_statistics():
    N, M = map(int, input().split())
    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    arr = np.array(matrix)

    mean_value = np.mean(arr, axis=1)
    var_value = np.var(arr, axis=0)
    std_value = np.std(arr, axis=None)

    return mean_value, var_value, std_value

if __name__ == '__main__':
    mean_value, var_value, std_value = calculate_statistics()
    print(mean_value)
    print(var_value)
    print(std_value)