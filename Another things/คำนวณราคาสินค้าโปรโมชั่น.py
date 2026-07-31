abc=input().split()
abclist=[0,0,0]
a=int(abc[0])
b=int(abc[1])
c=int(abc[2])
abclist[0]+=a
abclist[1]+=b
abclist[2]+=c
total=(25*a)+(40*b)+(55*c)
if sum(abclist) >= 3:
    total=total - (total*0.1)
print(int(total))
