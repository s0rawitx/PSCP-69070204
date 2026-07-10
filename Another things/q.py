x=int(input())
y=int(input())
if not x and not y:
    print("Origin")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x <= 0 and (y > 0 or y < 0):
    print("Y")
elif (x > 0 or x < 0) and y <=0:
    print("X")