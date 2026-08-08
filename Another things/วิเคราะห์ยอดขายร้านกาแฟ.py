'''test'''
n=int(input())
profitxd=[]
for i in range(n):
    profit=int(input())
    profitxd.append(profit)
average=sum(profitxd)/len(profitxd)

print(sum(profitxd))
print(max(profitxd))
print(min(profitxd))
print(f"{average:.1f}")
