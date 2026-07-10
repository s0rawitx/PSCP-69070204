n = int(input())
if n == 1:
    print(1)
else:
    total_digits = 0
    for i in range(1, n+1):
        total_digits += len(str(i))
    total_operators = n
    print(total_digits + total_operators)
