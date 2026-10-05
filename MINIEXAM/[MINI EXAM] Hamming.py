'''aaa'''
s1=input()
s2=input()
count=0
huh=len(s1)
for i in range(huh):
    if s1[i] != s2[i]:
        count+=1
print(count)
