number=input().replace(' ','')
number=number.replace("[","").replace("]","").split(",")
result=[]
for i in number:
    if not int(i)%2:
        result.append(i)
if result:
    for answer in result:
        print(answer)
else:
    print("Nope")
