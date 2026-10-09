cal=0
while True:
    command=int(input())
    if command==1:
        cal+=100
    elif command==2:
        cal+=120
    elif command==3:
        cal+=200
    elif command==4:
        cal+=60
    else:
        print("Bye Bye")
        print("Total Calories:",cal)
        break
