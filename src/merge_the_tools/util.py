
def merge_the_tools(string, k):

    n = len(string)

    for i in range(0, n, k):

        substring = string[i:i+k]
        unique_string = ""

        for ch in substring:

            if ch not in unique_string:
                unique_string = unique_string + ch

        print(unique_string)


if __name__ == "__main__":

    string = input()
    k = int(input())
    merge_the_tools(string, k)


