a = input().strip()
b = input().strip()
c = input().strip()

p = [a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a]

r = p[0]
if p[1] > r:
    r = p[1]
if p[2] > r:
    r = p[2]
if p[3] > r:
    r = p[3]
if p[4] > r:
    r = p[4]
if p[5] > r:
    r = p[5]

print(int(r))