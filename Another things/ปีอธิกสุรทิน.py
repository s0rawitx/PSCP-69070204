year=int(input())
if year > 1582:
    if not year % 400:
        print("yes")
    elif not year % 4:
        if not year % 100:
            print("no")
        else:
            print("yes")
else:
    if not year % 4:
        print("yes")
    else:
        print("no")
