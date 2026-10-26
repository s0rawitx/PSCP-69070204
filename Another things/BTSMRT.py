'''i hate ภาษาไทย bro '''
day=input()
age=float(input())
height=float(input())
if age < 14 and height < 90:
    print("FREE")
elif age < 14:
    if day=="Children Day":
        if height <= 140:
            print("FREE")
        else:
            print("PAY")
    else:
        print("PAY")
elif age >=60:
    if day=="Senior Day":
        print("FREE")
    else:
        print("PAY")
else:
    print("PAY")
