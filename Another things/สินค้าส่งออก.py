'''dwada'''
rob=int(input())
lit=[]
odd=0
even=0
for _ in range(rob):
    if not _:
        pass
    product=int(input())
    lit.append(product)
    if product % 2:
        odd+=1
    else:
        even+=1
print(f"SUM {sum(lit)}")
print(f"EVEN {even}")
print(f"ODD {odd}")
