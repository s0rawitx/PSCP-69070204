L, N = map(int, input().split())

p = 1
while (p * L) * (p * L + 1) // 2 < N:
    p += 1

print(p)