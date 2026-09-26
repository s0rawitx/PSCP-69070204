'''w'''
first,goal=map(int,input().split())
total_distant=first
total_jump=1
fail=False
while total_distant < goal:
    first-=2
    if first <= 0:
        fail=True
        break
    total_distant+=first
    total_jump+=1
if fail:
    print(-1)
else:
    print(total_jump)
