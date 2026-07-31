mook=input().split()
milkandsweetness=input().split()
mooktype=mook[0]
mookG=float(mook[1])
milk=milkandsweetness[0]
sweetness=float(milkandsweetness[1])
cc=float(milkandsweetness[2])
total=0
if milk == 'R':
    if sweetness==1:
        total+=12*cc
    elif sweetness==2:
        total+=18*cc
    else:
        total+=25*cc
elif milk == 'T':
    if sweetness==1:
        total+=15*cc
    elif sweetness==2:
        total+=20*cc
    else:
        total+=30*cc
elif milk =='M':
    if sweetness==1:
        total+=10*cc
    elif sweetness==2:
        total+=15*cc
    else:
        total+=20*cc
if mooktype=='H':
    total+=5*mookG
elif mooktype=='O':
    total+=3*mookG
else:
    total+=2*mookG
if total.is_integer():
    print(int(total))
else:
    print(total)
