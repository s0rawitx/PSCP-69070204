'''dada'''
n = int(input())
if n < 2:
    print("NO")
elif n == 2:
    print("YES")
elif not n % 2:
    print("NO")
else:
    is_prime = True
    limit = int(n ** 0.5)
    for i in range(3, limit + 1, 2):
        if not n % i:
            is_prime = False
            break
    if is_prime:
        print("YES")
    else:
        print("NO")
