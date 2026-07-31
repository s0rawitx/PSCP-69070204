'''ggss'''
temp=int(input())
status=input().lower()
if temp<=0 and status=="c" or (temp<=32 and status=='f'):
    print("solid")
elif temp>=100 and status=='c' or (temp>=212 and status=='f'):
    print("gas")
elif 0 < temp < 100 and status=='c' or 32 < temp < 212 and status=='f':
    print("liquid")
