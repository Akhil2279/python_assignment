
from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    time1 = datetime.strptime(t1, format_string)
    time2 = datetime.strptime(t2, format_string)
    
    difference = abs(int((time1 - time2).total_seconds()))    
    return difference


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        t1 = input()
        t2 = input()
        
        result = time_delta(t1, t2)
        print(result)


