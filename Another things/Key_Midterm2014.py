'''dada'''
number=input()
su=0
for num in number:
    su+=int(num)
ten=int(number[10:])*10
result=su+ten
if len(str(result)) > 4:
    print(str(result)[-4:])
elif result < 1000:
    result+=1000
    print(result)
else:
    print(result)
