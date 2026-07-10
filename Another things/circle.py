import math
x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
t1=(x2-x1)**2
t2=(y2-y1)**2
distance=math.sqrt(t1+t2)
sum_r=r1+r2
if distance <= sum_r:
    print("overlapping")
else:
    print("no overlapping")
