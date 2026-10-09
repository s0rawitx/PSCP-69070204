'''adad'''
count=0
male=0
female=0
male_list=[1,3,5,7,9]
female_list=[0,2,4,6,8]
while True:
    command=input()
    if int(command)<0:
        break
    elif int(command[-1]) in male_list:
        male+=1
        count+=1
    elif int(command[-1]) in female_list:
        female+=1
        count+=1
print(male,female,count)
