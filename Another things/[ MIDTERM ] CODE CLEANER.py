s = input()
letters = 0
digits = 0
res = ""
for ch in s:
    if "a" <= ch <= "z" or "A" <= ch <= "Z":
        letters += 1
        res += ch.upper()
    elif "0" <= ch <= "9":
        digits += 1
        res += ch
    else:
        if not res.endswith("-"):
            res += "-"
res = res.strip("-")
if not res:
    res = "NONE"
print("CODE =", res)
print("LETTERS =", letters)
print("DIGITS =", digits)
