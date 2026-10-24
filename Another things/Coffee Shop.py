'''dadad'''
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = int(input())

promo1 = a + a * (1 - b / 100) * (e - 1)

subtotal = a * e
if subtotal >= d:
    promo2 = subtotal * (1 - c / 100)
else:
    promo2 = subtotal

if promo1 < promo2:
    print(1)
    print(f"{promo1:.2f}")
else:
    print(2)
    print(f"{promo2:.2f}")
