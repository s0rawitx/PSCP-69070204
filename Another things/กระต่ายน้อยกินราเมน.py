'''ttt'''
scale , ramentype=input().split()
top=input().split()
name=top[0]
if len(top) > 1:
    quantity=top[1]
else:
    quantity=0
topping={"N": 0, 
         "P": 15,
         "E" : 10
        }
ramen={
    "S" : {"R" : 60,"T" : 80},
    "M" : {"R" : 80,"T" : 100},
    "L" : {"R" : 100,"T" : 120}
}
cal=ramen[scale][ramentype]+(topping[name]*int(quantity))
print(cal)
