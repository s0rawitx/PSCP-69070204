num=input().split()
positive=0
negative=0
zero=0
for number in num:
    if int(number) < 0:
        negative+=1
    elif int(number) > 0:
        positive+=1
    else:
        zero+=1
print(f'Positive: {positive}')
print(f"Negative: {negative}")
print(f"Zero: {zero}")
