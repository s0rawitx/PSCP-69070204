'''ddada'''
n = int(input())

if n == 1:
    print(1)
else:
    total_digits = 0
    length = 1
    start = 1
    while start <= n:
        end = start * 10 - 1
        if n < end:
            end = n
        count = end - start + 1
        total_digits += count * length
        start *= 10
        length += 1

    ans = total_digits + n
    print(ans)
