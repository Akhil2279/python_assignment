
import numpy as np

def array():
    N, M = map(int, input().split())

    values = []

    for _ in range(N):
        values.append(list(map(int, input().split())))

    arr = np.array(values)
    return np.max(np.min(arr, axis=1))

if __name__ == '__main__':
    result = array()
    print(result)
