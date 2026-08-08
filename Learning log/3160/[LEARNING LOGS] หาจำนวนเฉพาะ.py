'''what'''
start, end = input().split()
start = int(start)
end = int(end)
ans = []

for i in range(start, end + 1):
    if i <= 1:
        continue
    prime = True
    for j in range(2, i):
        if not i % j:
            prime = False 
            break
    if prime:
        ans.append(i)

if ans:
    print(*ans)
print(f"Total primes: {len(ans)}")
