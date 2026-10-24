'''dadad'''
item={}
while True:
    command=input().split()
    if command[0]=="END":
        break
    if command[0]=="ADD":
        name=command[1]
        quantity=command[2]
        if name in item:
            item.update({name:int(item[name])+int(quantity)})
        else:
            item[name]=int(quantity)
    elif command[0]=="REMOVE":
        name=command[1]
        quantity=command[2]
        if name in item:
            if item[name] >= int(quantity):
                item[name]-=int(quantity)
            else:
                item[name]=0
                print(f"Not enough stock for {name}")
        else:
            item[name]=0
            print(f"Not enough stock for {name}")
    elif command[0]=="CHECK":
        lol=[]
        yes=True
        for key,value in item.items():
            if int(value) >= 5:
                continue
            lol.append(key)
            yes=False
        lol.sort(key=ascii)
        if yes:
            print("All stocks are sufficient")
        else:
            for i in lol:
                print(i)
    elif command[0]=="REPORT":
        haha=[]
        for n,val in item.items():
            haha.append((n,val))
        haha.sort(key=ascii)
        for kkk,hello in haha:
            print(f"{kkk}: {hello}")
