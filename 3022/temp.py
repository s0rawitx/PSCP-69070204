'''ddd'''
n = float(input())
before = input().upper()
after = input().upper()
if before == "C":
    if after == "F":
        n = (n*(9/5))+32
    elif after == "K":
        n = n + 273.15
    elif after == "R":
        n = (n+273.15) * (9/5)
elif before == "K":
    if after == "F":
        n = ((9/5)*n) - 459.67
    elif after == "C":
        n = n - 273.15
    elif after == "R":
        n = n*(9/5)
elif before == "F":
    if after == "K":
        n = (n-32)*(5/9)+273.15
    elif after == "C":
        n = (5/9) *(n-32)
    elif after == "R":
        n = n + 459.67
elif before == "R":
    if after == "K":
        n = n * (5/9)
    elif after == "C":
        n = ((5/9)*n) - 273.15
    elif after == "F":
        n = n - 459.67
print(f"{n:.2f}")
