Alice=int(input())
Bob=int(input())
cream=int(input())
Alice_distant=abs(Alice-cream)
bob_distant=abs(Bob-cream)
if Alice_distant < bob_distant:
    print("Alice",Alice_distant)
elif bob_distant < Alice_distant:
    print("Bob",bob_distant)
else:
    print("Sundaes",bob_distant)
