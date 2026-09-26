'''adada'''
n, k, t = map(int, input().split())
current = 1
count = 1
if current != t:
    while True:
        current = (current + k - 1) % n + 1
        if current == t:
            count += 1
            break
        if current == 1:
            break
        count += 1
print(count)
