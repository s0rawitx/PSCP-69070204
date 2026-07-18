'''divide 10'''
n=int(input())
m=[]
for i in range(n+1):
    if not i%10:
        m.append(i)
m.reverse()
print(*m)
