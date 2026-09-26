'''ww'''
def main():
    name=input()
    age=int(input())
    salary=float(input())
    status=input().upper()
    family=int(input())
    valid=True
    if age < 18:
        stats="NOT ELIGIBLE"
        valid=False
    elif status=='Y':
        stats="GOLD"
    elif salary <=15000:
        stats="GOLD"
    elif salary <= 30000:
        stats="SILVER"
    else:
        valid=False
        stats="NOT ELIGIBLE"
    if stats=="GOLD":
        bonus=3000
    elif stats=="SILVER":
        bonus=1500
    if valid:
        if family >= 3:
            bonus+=500
    if valid:
        print(f"{name} {stats} {bonus}")
    else:
        print(f"{name} {stats}")
main()
