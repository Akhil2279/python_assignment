
from collections import OrderedDict

def count_words():
    n = int(input())
    word_count = OrderedDict()

    for _ in range(n):
        word = input().strip()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_count = len(word_count)
    occurrences = list(word_count.values())
    return distinct_count, occurrences

if __name__ == '__main__':
    distinct_count, occurrences = count_words()
    print(distinct_count)
    print(*occurrences)


