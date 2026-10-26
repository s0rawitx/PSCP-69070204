'''dadadad'''
def domestic(phone):
    '''dadadadad'''
    result1=''
    count=0
    if len(phone) == 9:
        result1+=phone[0]+" "
        for test in phone[1:]:
            if count==4:
                result1+=" "+test
                count=0
            else:
                result1+=test
                count+=1
    elif len(phone) > 9:
        result1+=phone[:2]+" "
        for haha in phone[2:]:
            if count==4:
                result1+=" "+haha
                count=0
            else:
                result1+=haha
                count+=1
    return result1

def international(phone):
    '''dadad'''
    count=0
    result=''
    count=0
    if len(phone) > 9:
        result+="+66"+phone[1]+" "
        for test in phone[2:]:
            if count==4:
                result+=" "+test
                count=0
            else:
                result+=test
                count+=1
        return result
    result+="+66"+" "
    for aa in phone[1:]:
        if count==4:
            result+=" "+aa
            count=0
        else:
            result+=aa
            count+=1
    return result

def main():
    '''dadadad'''
    phone=input()
    t=input()
    if t=="Domestic":
        print(domestic(phone))
    elif t=="International":
        print(international(phone))
main()
