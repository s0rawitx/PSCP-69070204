rahut=input()

if rahut[:2]=="68" and rahut[2:4]=="07" and 1 <= int(rahut[4:]) <= 328:
    print("Yes")
else:
    print("No")