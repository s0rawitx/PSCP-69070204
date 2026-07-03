c1=input()
c2=input()
color=["Red","Yellow","Blue"]
if c1 in color and c2 in color:
    if c1 =='Red' and c2 =='Yellow' or (c1=='Yellow' and c2 =='Red'):
        print("Orange")
    elif c1 =='Red' and c2 =='Blue' or (c1=='Blue' and c2=='Red'):
        print("Violet")
    elif c1 =='Yellow' and c2 =='Blue' or (c1=='Blue' and c2=='Yellow'):
        print("Green")
    elif c1 in c2:
        print(c1)
else:
    print("Error")