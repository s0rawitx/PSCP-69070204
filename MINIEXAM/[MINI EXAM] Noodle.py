price=int(input())
money=int(input())
diff=money-price
if diff==0:
    print("Good!")
elif money<price:
    print("Need more cash!")
else:
    print(diff)