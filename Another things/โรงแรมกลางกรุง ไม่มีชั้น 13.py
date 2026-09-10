'''test'''
room=input()
first=int(room[0])
sec=int(room[1])
third=int(room[2])
forth=int(room[3])
fifth=int(room[4])
result=''

#first_digit
if first > 5:
    result+="9"
elif sec > 5:
    result+="10"
elif third > 5:
    result+="11"
elif forth > 5:
    result+="12"
elif fifth > 5:
    result+="14"
else:
    result+='13'
#second_digit
if room==room[::-1]:
    if first+fifth > 5:
        result+="1"
    elif sec*forth > 5:
        result+="2"
    else:
        result+="0"
else:
    if fifth==0:
        fifth=1
    if first//fifth > 5:
        result+="1"
    elif sec-fifth > 5:
        result+="2"
    else:
        result+='0'
#third_digit
if first+sec+third+forth+fifth > 25:
    result+="1"
elif first*sec*third*forth*fifth > 55:
    result+="2"
else:
    result+="0"
print(result)
