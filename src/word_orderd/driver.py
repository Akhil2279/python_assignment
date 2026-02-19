
from util import count_words

if __name__ == "__main__":

    distinct_count, occurrences = count_words()
    print(distinct_count)
    print(*occurrences)


