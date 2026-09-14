wtf=input()
wtf=wtf.replace("[","").replace("]","").split(",")
for number in wtf:
    print(str(number)[-1])
