x=int(input())
y=int(input())
a=int(input())
z=int(input())
if z >= y and z>=x:
    free= (z // x)*(x-y)*a
    price=(z*a)-free
else:
    price=(z*a)
print(price)