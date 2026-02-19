
import numpy
numpy.set_printoptions(legacy='1.13')

def process_array(values):
    A = numpy.array(values)
    
    floor_values = numpy.floor(A)
    ceil_values = numpy.ceil(A)
    rint_values = numpy.rint(A)
    
    return floor_values, ceil_values, rint_values

if __name__ == '__main__':
    values = list(map(float, input().split()))
    floor_values, ceil_values, rint_values = process_array(values)
    
    print(floor_values)
    print(ceil_values)
    print(rint_values)


