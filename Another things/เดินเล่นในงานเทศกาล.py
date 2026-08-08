'''aaawda'''
walk=input().lower()
x=0
y=0
for char in walk:
    if char == 'n':
        y+=1
    elif char=='s':
        y-=1
    elif char=='e':
        x+=1
    elif char=='w':
        x-=1
    else:
        continue
d=abs(x)+abs(y)
print(x,y,d)