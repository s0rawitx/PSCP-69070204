n=input().split()
r=int(n[0])
x=int(n[1])
y=int(n[2])
left=(x**2)+(y**2)
right=r**2
if left == right:
    print("ON")
elif left < right:
    print("IN")
else:
    print("OUT")
