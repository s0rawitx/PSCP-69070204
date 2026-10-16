'''dadad'''
n = int(input())
animals = {}
for _ in range(n):
    line = input().strip().strip("{}")
    name, code = line.split(":")
    animals[name.strip().strip('"')] = code.strip().strip('"')

if "Cat01" not in animals.values() and "Garfield" not in animals:
    animals["Garfield"] = "Cat01"
if "Fox01" not in animals.values() and "Fubuki" not in animals:
    animals["Fubuki"] = "Fox01"

cats = {k: v for k, v in animals.items() if v.startswith("Cat")}
foxes = {k: v for k, v in animals.items() if v.startswith("Fox")}

print("Cat :", len(cats))
print("Fox :", len(foxes))

for group in (cats, foxes):
    for name, code in sorted(group.items(), key=lambda x: int(x[1][3:])):
        print(name, ":", code)
