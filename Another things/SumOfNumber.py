jaja=0
goal=int(input())
while True:
    command=int(input())
    if command==-1:
        print(jaja)
        break
    jaja+=command 
    if jaja==goal:
        print(jaja)
        break