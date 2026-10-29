game=input()
round_diff=int(input())
if game=="Rov":
    if round_diff >=2:
        print("GGEZ")
    else:
        print("GGWP")
elif game=="Valorant":
    if round_diff >=7:
        print("GGEZ")
    else:
        print("GGWP")
