'''40 บรรทัด brather'''
s1=input()
s2=input()
valid=["l","o","v","e"]
result=''
if len(s1)<len(s2):
    for i in range(len(s2)):
        if len(s1)==len(s2):
            break
        s1+=s1[i]
elif len(s1)>len(s2):
    for i in range(len(s1)):
        if len(s1)==len(s2):
            break
        s2+=s2[i]
s1_len=len(s1)
for i in range(s1_len):
    if s1[i].lower() in valid or s2[i].lower() in valid:
        result+="w"
    else:
        result+="$"
current_max=0
counting=0
tid=False
result_len=len(result)
if result.count("w")%2:
    for k in range(result_len):
        if result[k]=='w':
            counting+=1
        else:
            counting=0
        if counting>current_max:
            current_max=counting
    result+=str(current_max)
elif not result.count("w")%2:
    for j in range(len(result)-1):
        if result[j] == "w" and result[j+1] == "w":
            tid=True
            break
    if not tid:
        result+="#"
print(result)
