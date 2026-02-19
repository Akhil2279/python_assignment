
from util import time_delta

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        t1 = input()
        t2 = input()
        
        result = time_delta(t1, t2) 
        print(result)
