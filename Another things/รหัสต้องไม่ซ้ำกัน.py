'''testing'''
n=int(input())
number=input().split()
result=[]
for i in range(n):
    if number.count(number[i])==1:
        result.append(int(number[i]))
result.sort()
print(*result)
