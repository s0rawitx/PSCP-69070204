what={}
alive=[]
dead=[]
deadmemory={}
while True: 
    yuh=input().replace("{","").replace("}","").replace(" ","")\
        .replace('"', '').replace("'", '').split(":")
    if yuh[0]=='Start':
        break
    what[yuh[0]]=yuh[1]
    alive.append(yuh[0])


while True:
    die=input()
    if die=='End':
        break
    dead.append(die)
    alive.remove(die)

count=0

for test in dead:
    try:
        deadmemory[test]=what[test]
        what.pop(test)
    except KeyError:
        pass


for haha in what.values():
    if haha == "Impostor":
        count+=1

alive.sort(key=ascii)
print(f"{count} Impostor Remains")
print("***Alive***")
for hahaha in alive:
    print(f'{hahaha} : {what[hahaha]}')
print("***Dead***")
dead.sort(key=ascii)
for key in dead:
    print(f"{key} : {deadmemory[key]}")