'''aoaoao'''
N=str(input().lower())
a=0
e=0
i=0
o=0
u=0
for char in N:
    if char == 'a':
        a+=1
    elif char =='e':
        e+=1
    elif char == 'i':
        i+=1
    elif char =='o':
        o+=1
    elif char =='u':
        u+=1
    else:
        continue
if a:
    print(f"a : {a}")
if e:
    print(f"e : {e}")
if i:
    print(f"i : {i}")
if o:
    print(f"o : {o}")
if u:
    print(f"u : {u}")
