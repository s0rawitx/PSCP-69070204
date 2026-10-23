import json
data=json.loads(input())
minimum=float(input())
aka=[]
for name,score in data.items():
    if float(score) >= minimum:
        aka.append((int(name),score))
aka.sort()
if aka:
    for test,eiei in aka:
        print(f"{test}	{eiei:.2f}")
else:
    print("Nope")