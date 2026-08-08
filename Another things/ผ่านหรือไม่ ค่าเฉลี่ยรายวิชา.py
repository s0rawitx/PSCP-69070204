'''afaa'''
subject=int(input())
what=[]
for i in range(subject):
    if not i:
        pass
    score=int(input())
    what.append(score)
average_score=sum(what)/len(what)
print(f"{average_score:.1f}")
if average_score >= 60:
    p=True
    for score in what:
        if score < 50:
            p=False
            break
else:
    p=False

if p:
    print("PASS")
else:
    print("FAIL")
