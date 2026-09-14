group1=int(input())
group2=int(input())
dupe=[]
check=set()
cheater=set()
for _ in range(group1+group2):
    dupe.append(input())
for name in dupe:
    if name in check:
        cheater.add(name)
    else:
        check.add(name)
cheater=list(cheater)
cheater.sort(reverse=True)
if len(cheater)==0:
    print("Nope")
else:
    print(*cheater,sep="\n")
