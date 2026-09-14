k = int(input())
n = int(input())
mid = n // 2
for i in range(n):
    leading_spaces = " " * abs(mid - i)
    asterisks = "*" * k
    print(leading_spaces + asterisks)
