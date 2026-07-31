status=input().split()
position=status[0].lower()
age=int(status[1])
salary=int(status[2])
total_bonus=0
if position=='m':
    total_bonus+=1500
elif position=='b':
    total_bonus+=1000
elif position=="g":
    total_bonus+=500
if position=='m':
    if age < 5:
        total_bonus+=salary*(0.06)
    elif age <= 10:
        total_bonus+=salary*(0.08)
    else:
        total_bonus+=salary*(0.10)
elif position=='b':
    if age < 5:
        total_bonus+=salary*(0.05)
    elif age <= 10:
        total_bonus+=salary*(0.06)
    else:
        total_bonus+=salary*(0.07)
elif position=='g':
    if age < 5:
        total_bonus+=salary*(0.04)
    elif age <= 10:
        total_bonus+=salary*(0.05)
    else:
        total_bonus+=salary*(0.06)
print(int(total_bonus))
