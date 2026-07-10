fp = int(input())
cap = int(input())
dp = int(input())
d = int(input())
if d == 0:
    print(0)
else:
    buy = d - 1
    if cap > 0:
        h = buy // cap
        h_l = buy % cap
        per_set = (cap - 1) * fp + dp
        total = (h * per_set) + (h_l * fp)
        print(total + fp)
    else:
        print(d * fp)
