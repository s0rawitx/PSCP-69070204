result=[]
while True:
    string=input()
    if string=="NULL":
        break
    result.append(string)
result.reverse()
for i in result:
    print(i)
