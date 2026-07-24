bruh=[]
bruh.append(int(input()))
bruh.append(int(input()))
bruh.append(int(input()))
even=0
odd=0
for i in bruh:
    if not i % 2:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
