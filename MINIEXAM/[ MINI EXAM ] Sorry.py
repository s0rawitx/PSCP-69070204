items=[]
while True:
    item=input()
    if item=="End":
        break
    items.append(item)
    if item=="Sorry":
        items.pop()
        items.pop()
print(", ".join(items))