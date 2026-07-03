ra=int(input())
rb=int(input())
string=input().upper()
t1=pow(10,(ra-rb)/400)
t2=pow(10,(rb-ra)/400)
ea=1/(1+t2)
eb=1/(1+t1)
if string =='A':
    print(f"{ea:.2f}")
elif string =='B':
    print(f"{eb:.2f}")
else:
    print("Error")
