import math
r=float(input())
a=float(input())
b=float(input())
circle=2*(math.pi)*r
rectangle=(a*2)+(b*2)
diff=abs(circle-rectangle)

if circle > rectangle:
    print("Circle is longer")
    print(f"{diff:.5f}")
elif rectangle > circle:
    print("Rectangle is longer")
    print(f"{diff:.5f}")
else:
    print("Equal")
    print(f"{diff:.5f}")
