'''adada'''
a = int(input())
b = int(input())
if b % 2 != 0 or b < 2 * a or b > 4 * a:
    print("Impossible")
else:
    rabbits = (b - 2 * a) // 2
    birds = a - rabbits
    print(rabbits, birds)
