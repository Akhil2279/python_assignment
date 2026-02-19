
from util import process_array

if __name__ == '__main__':
    values = list(map(float, input().split()))
    floor_values, ceil_values, rint_values = process_array(values)
    
    print(floor_values)
    print(ceil_values)
    print(rint_values)

    