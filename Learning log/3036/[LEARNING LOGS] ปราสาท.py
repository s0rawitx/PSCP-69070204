import math
n=int(input())
row=math.ceil(n**0.5)
last=row**2
if row != 1:
    if not (last-n) % 2:
        print((2*row)-2)
    else:
        print((2*row)-3)
else:
    print(0)
