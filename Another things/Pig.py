n=int(input())
weight=input().split()
cu=list(zip(weight[::2],weight[1::2]))
result=[]
for i in cu:
    result.append(max(i, key=int))
num_result=list(map(int,result))
if len(result) > 1:
    print(" + ".join(result)+" = "+str(sum(num_result)))
else:
    print(*result)
