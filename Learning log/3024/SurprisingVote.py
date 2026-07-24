'''dadad'''
vote=float(input())
high=float(input())
remain=vote-high
mid=min(high, remain)
low=remain-mid
if high - low > 2:
    print("Surprising")
else:
    print("Not surprising")
