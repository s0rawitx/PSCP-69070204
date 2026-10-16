'''dada'''
def solve():
    '''dada'''
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))

        # เรียงตาม x + y จากน้อยไปมาก และถ้าเท่ากันให้เรียง y จากมากไปน้อย
        points.sort(key=lambda p: (p[0] + p[1], -p[1]))

        for x, y in points:
            print(f"{x} {y}")
solve()
    