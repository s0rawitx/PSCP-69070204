seat=int(input())
while seat != 0:
    people=input().split()
    age=int(people[0])
    ticket=int(people[1])
    if age < 15:
        print("-1")
    elif ticket > seat:
        print("-2")
    elif 15 <= age <= 22:
       price=(150-(150*0.2))*ticket
       seat=seat-ticket
       print(int(price),seat)
    elif age >= 60:
        price=(150-(150*0.5))*ticket
        seat=seat-ticket
        print(int(price),seat)
    else:
        price=150*ticket
        seat=seat-ticket
        print(price,seat)
