'''hew'''
huh=[]
n1=huh.append(int(input()))
n2=huh.append(int(input()))
n3=huh.append(int(input()))
if len(set(huh)) == 1:
    print("all the same")
elif len(set(huh)) == 2:
    print("neither")
else:
    print("all different")
