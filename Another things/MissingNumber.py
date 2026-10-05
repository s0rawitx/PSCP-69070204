number=[]
result=[]
max_num=int(input())
while True:
    other_num=int(input())
    if other_num==0:
        break
    else:
        number.append(other_num)
for i in range(1,max_num+1):
    if i not in number:
        result.append(i)
for uh in result:
    print(uh)