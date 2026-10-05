'''aadada'''
card=input().upper()
special=["A","J","Q","K"]
full_name=["ace","jack","queen","king"]
if len(card) == 3:
    cardtype=card[2]
    num=card[:2]
else:
    cardtype=card[1]
    num=card[0]
DIAMOND="of diamonds"
HEARTS="of hearts"
SPADE="of spades"
CLUBS="of clubs"
if cardtype == "D":
    if num in special:
        index=special.index(num)
        print(full_name[index],DIAMOND)
    else:
        print(num,DIAMOND)
elif cardtype == "H":
    if num in special:
        index=special.index(num)
        print(full_name[index],HEARTS)
    else:
        print(num,HEARTS)
elif cardtype == "S":
    if num in special:
        index=special.index(num)
        print(full_name[index],SPADE)
    else:
        print(num,SPADE)
else:
    if num in special:
        index=special.index(num)
        print(full_name[index],CLUBS)
    else:
        print(num,CLUBS)
