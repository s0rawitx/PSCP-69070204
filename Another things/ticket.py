'''ggg'''
ageandday=input().split()
promo=False
if ageandday[1].lower() =='wed':
    promo=True
if int(ageandday[0]) < 5:
    print(0)
elif 5 <= int(ageandday[0]) <= 18:
    if promo:
        print(50)
    else:
        print(100)
elif int(ageandday[0]) >= 19:
    if promo:
        print(75)
    else:
        print(150)
