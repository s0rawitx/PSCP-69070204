'''ddd'''
money=float(input("Enter number money withdraw : "))
b1000_count=0
b500_count=0
b100_count=0
if money <= 50 or money > 20000 or money%100:
    print("ERROR")
else:
    while money:
        if money // 1000:
            b1000_count+=1
            money-=1000
        elif money // 500:
            b500_count+=1
            money-=500
        elif money // 100:
            b100_count+=1
            money-=100
        else:
            break
if b1000_count:
    print(f"1000 = {b1000_count}")
if b500_count:
    print(f"500 = {b500_count}")
if b100_count:
    print(f"100 = {b100_count}")
