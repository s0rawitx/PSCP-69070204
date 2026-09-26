'''adadada'''
def main():
    '''adad'''
    unit=float(input())
    towhat=input().upper()
    fromwhat=input().upper()
    if fromwhat=='NIU':
        unit=unit*1
    elif fromwhat=='KUEP':
        unit=unit*12
    elif fromwhat=='SOK':
        unit=unit*24
    elif fromwhat=='WA':
        unit=unit*96
    else:
        unit=unit*1920
    if towhat=='NIU':
        result=unit
    elif towhat=="KUEP":
        result=unit/12
    elif towhat=="SOK":
        result=unit/24
    elif towhat=='WA':
        result=unit/96
    else:
        result=unit/1920
    print(f"{result:.4f}")
main()
