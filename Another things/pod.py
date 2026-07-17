'''dadadadadadad'''
n=input().split()
allrow=int(n[1])
rows_count = [0] * allrow
for i in range(int(n[0])):
    row=int(input())
    rows_count[row-1]+=1
    if 0 not in rows_count:
        rows_count=[x-1 for x in rows_count]
    else:
        continue
print(sum(rows_count))
