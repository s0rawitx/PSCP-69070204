'''ggg'''
km=int(input())
fare=0
if km <= 0:
    fare=0
elif km <= 1:
    fare=35
elif 1 < km <= 10:
    fare=35+((km*5)-(5))
else:
    fare=35+45+((km-10)*8)
print(fare)
