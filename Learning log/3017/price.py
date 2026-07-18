p=int(input())
service=p*(10/100)
if service<50:
    service = 50
elif service > 1000:
    service = 1000
serp=p+service
vat=serp*(7/100)
result=serp+vat
print(f"{result:.2f}")