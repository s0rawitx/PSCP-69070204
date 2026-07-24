'''xix'''
n=int(input())
gg=["hehe","I","II","III","IV","V","VI","VII","VIII","IX"]
if n < 0:
    print("Error : Please input positive number")
elif n == 0:
    print("Error : Out of range")
elif n > 9:
    print("Error : Out of range")
else:
    print(gg[n])
