test=int(input())
eiei=[]
for _ in range(test):
    huh=input()
    eiei.append(huh)
eiei.sort(key=len)
print("\n".join(eiei))