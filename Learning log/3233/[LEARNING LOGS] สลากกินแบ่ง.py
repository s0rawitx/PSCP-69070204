'''gg'''
result=input()
buy=input()
result_char=result[0]
result_num=result[2:]
buy_char=buy[0]
buy_num=buy[2:]
if buy==result:
    print("1000000")
elif buy_num == result_num and buy_char != result_char:
    print("100000")
elif buy_char==result_char:
    if buy_num[-3:] == result_num[-3:]:
        print("2000")
    elif buy_num[-2:] == result_num[-2:]:
        print("1000")
    else:
        print("20")
elif buy_char != result_char:
    if buy_num[-3:] == result_num[-3:]:
        print("200")
    elif buy_num[-2:] == result_num[-2:]:
        print("100")
    else:
        print(0)
