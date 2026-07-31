'''gg'''
n=int(input())
vowel=["a","e","i","o","u"]
count=0
for _ in range(n):
    if not _:
        pass
    anksorn=input().lower()
    if anksorn in vowel:
        count+=1
    else:
        continue
print(count)
