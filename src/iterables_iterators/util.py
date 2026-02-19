
from itertools import combinations

def probability_of_a():

    n = int(input())
    letters = input().split()
    k = int(input())

    total_combinations = list(combinations(range(n), k))
    favorable = 0

    for combo in total_combinations:
        for index in combo:
            if letters[index] == 'a':
                favorable += 1
                break

    probability = favorable / len(total_combinations)
    
    return round(probability, 4)

if __name__ == '__main__':
    result = probability_of_a()
    print(result)

    