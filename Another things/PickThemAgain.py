'''esea'''
num=input().split(" ")
result=[]
for number in num:
    if not int(number)%5 or not int(number)%3:
        result.append(number)
result.reverse()
if result:
    for namber in result:
        print(namber)
else:
    print("Nope")
