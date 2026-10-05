'''adadad'''
num=int(input())
result=0
for i in range(1,num+1):
    if not i%3:
        result+=i
    elif not i%5:
        result+=i
print(result)