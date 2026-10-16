'''dada'''
REQUIRED_INGREDIENTS = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
}

REQUIRED_TASTES = {"Sweet", "Sour", "Salty"}

ingredients = set()
invalid_ingredient_found = False

while True:
    line = input().strip()
    if line == "Cook":
        break
    if line in REQUIRED_INGREDIENTS:
        ingredients.add(line)
    else:
        invalid_ingredient_found = True

tastes = set()
while True:
    line = input().strip()
    if line == "End":
        break
    tastes.add(line)

if invalid_ingredient_found:
    print("This is not Pad Thai!!!")
elif ingredients != REQUIRED_INGREDIENTS:
    print("This is bad!")
elif tastes == REQUIRED_TASTES:
    print("Delicious!")
else:
    print("Not Bad...")
