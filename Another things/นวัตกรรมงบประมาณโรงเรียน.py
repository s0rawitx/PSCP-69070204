'''huh'''
school_name = input().upper()
first_char = school_name[0]
last_char = school_name[-1]
ascii_first = ord(first_char)
ascii_last = ord(last_char)
length = len(school_name)
code_stage2 = []
for position in range(1, 11):
    base_val = position - 1
    #รหัสชั้นที่ 1
    if position % 2:
        val_stage1 = ascii_first + base_val
    else:
        val_stage1 = ascii_last - base_val
    #รหัสชั้นที่ 2
    remainder = val_stage1 % length
    if remainder > 9:
        remainder = remainder % 10
    code_stage2.append(remainder)
#รหัสชั้นที่ 3 ดึงกึ่งกลาง 6 ตัว (index 3-8 ถ้านับจากตารางจะอยู่ตรงกลางพอดี)
selected_code = code_stage2[2:8]
print(*selected_code,end=' ')
