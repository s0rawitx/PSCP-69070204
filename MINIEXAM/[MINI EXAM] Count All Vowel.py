lop=int(input())
vowel=["a","e","i","o","u"]
a=0
e=0
i=0
o=0
u=0
count=0
for _ in range(lop):
    alpha=input().lower()
    if alpha in vowel:
        count+=1
    if alpha=="a":
        a+=1
    elif alpha=='e':
        e+=1
    elif alpha=='i':
        i+=1
    elif alpha=='o':
        o+=1
    elif alpha=='u':
        u+=1
if a and e and i and o and u:
    print(count)
    print("YES")
else:
    print(count)
    print("NO")
