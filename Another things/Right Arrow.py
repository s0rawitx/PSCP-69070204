k = int(input())
n = int(input())
mid = n // 2
for i in range(n):
    if i <= mid:
        spaces = i
    else:
        spaces = (n - 1) - i
    print(" " * spaces + "*" * k)
