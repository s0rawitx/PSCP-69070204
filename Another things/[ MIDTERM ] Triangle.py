'''adadda'''
def main():
    '''dadad'''
    a=int(input())
    b=int(input())
    c=int(input())
    valid=True
    right=False
    highest=0
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        right=True
    if not a+b>c or not a+c>b or not b+c>a:
        valid=False
    if valid:
        if right:
            print("RIGHT TRIANGLE")
        elif a==b==c:
            print("EQUILATERAL")
        elif a==b or a==c or b==c:
            print("ISOSCELES")
        elif a != b != c:
            print("SCALENE")
    else:
        print("NOT A TRIANGLE")
main()
