A=int(input())
B=int(input())
divide=int(input())
sed=int(input())
ans=[]
for i in range(A,B+1):
    if i%divide==sed:
        ans.append(i)
    else:
        continue
print(len(ans))