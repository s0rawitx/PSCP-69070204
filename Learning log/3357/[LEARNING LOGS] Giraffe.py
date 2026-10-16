'''ddd'''
def solve():
    '''dadad'''
    n = int(input())
    heights = []
    for _ in range(n):
        heights.append(int(input()))
    if n == 1:
        print(1)
        return
    count = 0
    if heights[0] > heights[1]:
        count += 1

    if heights[n - 1] > heights[n - 2]:
        count += 1

    for i in range(1, n - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            count += 1
    print(count)
solve()
