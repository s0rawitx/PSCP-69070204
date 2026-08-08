'''aaaa'''
n = int(input())

total = 0
pattern = ""

for i in range(n):
    a = int(input())
    b = int(input())
    mx = max(a, b)
    
    total += mx
    
    if i == 0:
        pattern = str(mx)
    else:
        pattern += f" + {mx}"

if n == 1:
    print(total) 
else:
    print(f"{pattern} = {total}")
