import math
n1=input().split()
n2=input().split()
x1=int(n1[0])
x2=int(n2[0])
y1=int(n1[1])
y2=int(n2[1])
z1=int(n1[2])
z2=int(n2[2])
t1=(x2-x1)**2
t2=(y2-y1)**2
t3=(z2-z1)**2
d=math.sqrt(t1+t2+t3)
print(f"{d:.2f}")