vote=float(input())
high=float(input())
remain=vote-high
h1=remain//2
h2=(remain//2)+1
if high-h1 > 2:
    print("Surprising")
else:
    print("Not surprising")
