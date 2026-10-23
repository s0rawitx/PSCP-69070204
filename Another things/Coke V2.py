'''dadad'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not b or d <= b:
    print(d * a)
else:
    r = d - b
    disc = (r + b - 1) // b
    full = d - disc
    print(full * a + disc * c)
