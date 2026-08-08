'''ddaw'''
n=int(input())
total=0
for _ in range(n):
    command=input()
    if command == '+':
        total+=10
    elif command =='-':
        total-=5
print(total)
