'''dada'''
def solve():
    '''dada'''
    first_line = input().split()
    if not first_line:
        return

    n = int(first_line[0])
    s = int(first_line[1])

    next_student = [0] * (n + 1)
    for i in range(1, n + 1):
        next_student[i] = int(input())

    visited = [False] * (n + 1)
    current = s
    count = 0
    while current and not visited[current]:
        visited[current] = True
        count += 1
        current = next_student[current]

    print(count)


solve()
