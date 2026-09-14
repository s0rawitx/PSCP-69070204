what=input()
kuy=what.split()
index=int(input())
test=what.index(what[index])
araiwa=kuy.count(str(index))
for _ in range(int(araiwa)):
    print(str(test)*araiwa)
