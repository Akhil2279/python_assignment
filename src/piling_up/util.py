
def piling_up():

    t = int(input())

    results = []

    for _ in range(t):

        n = int(input())
        blocks = list(map(int, input().split()))

        left = 0
        right = n - 1
        last = float('inf')
        possible = True

        while left <= right:
            if blocks[left] >= blocks[right]:
                pick = blocks[left]
                left += 1
            else:
                pick = blocks[right]
                right -= 1

            if pick <= last:
                last = pick
            else:
                possible = False
                break

        if possible:
            results.append("Yes")
        else:
            results.append("No")

    return results

if __name__ == '__main__':
    results = piling_up()
    for result in results:
        print(result)

    
    