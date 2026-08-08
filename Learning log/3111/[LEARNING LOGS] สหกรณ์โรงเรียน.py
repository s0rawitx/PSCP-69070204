from decimal import Decimal, ROUND_HALF_UP
member=input().lower()
product=int(input())
total=0
for _ in range(product):
    if not _:
        pass
    price=Decimal(input())
    total+=price
if member == 'y':
        total=total-(total* Decimal("0.05"))
else:
    if total >=500:
        total=total-(total* Decimal("0.03"))
    else:
        pass
total=total.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
print(f"{total:.2f}")
