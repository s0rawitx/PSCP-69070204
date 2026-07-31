ein = input()
out = input()

hour, minute = ein.split('.')
outhour, outmin = out.split('.')

h_in, m_in = int(hour), int(minute)
h_out, m_out = int(outhour), int(outmin)

total_INtime = (h_in * 60) + m_in
total_OUTtime = (h_out * 60) + m_out
Total_all = total_OUTtime - total_INtime

invalid_time = (m_in >= 60 or m_out >= 60 or 
                h_in >= 24 or h_out >= 24 or 
                h_in < 0 or h_out < 0)

if Total_all < 0 or Total_all > 1440 or invalid_time:
    print("ERROR")
elif Total_all <= 15:
    print("FREE")
else:
    if Total_all % 60:
        hours = (Total_all // 60) + 1
    else:
        hours = Total_all // 60

    if hours <= 1:
        print(25)
    elif hours == 2:
        print(50)
    elif hours == 3:
        print(80)
    elif hours == 4:
        print(110)
    elif hours == 5:
        print(145)
    elif hours == 6:
        print(180)
    else:
        print(250)
