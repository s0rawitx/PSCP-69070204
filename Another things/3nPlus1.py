'''ggwp'''
count=0
while True:
    number=int(input())
    if not number:
        break
    while number !=1:
        if not number%2:
            number=number/2
            count+=1
        elif number%2:
            number=(number*3)+1
            count+=1
        if number==1:
            print(count+1)
            count=0
