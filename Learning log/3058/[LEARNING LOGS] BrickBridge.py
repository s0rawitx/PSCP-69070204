'''dddd'''
small=int(input())
b=int(input())
goal=int(input())
big=goal // 5
bigused=min(big,b)
remain=goal-(bigused*5)
if remain <= small:
    print(remain)
else:
    print(-1)
