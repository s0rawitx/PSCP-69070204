'''eaeae'''
s=input()
yo={}
for huh in s:
    yo[huh]=yo.get(huh,0)+1
result=[]
for test,count in yo.items():
    if count % 2:
        result.append(test)
if result:
    print("".join(result))
else:
    print("fully paired")
