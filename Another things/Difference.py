n=int(input())
m=int(input())
a=set()
b=set()
for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))
result=list(a-b)
result.sort()
print(*result)