'''gg'''
n=int(input())
result=''
for i in range(1,n+1):
    if i%5:
        result+="*"
    else:
        result+="X"
print(result)
