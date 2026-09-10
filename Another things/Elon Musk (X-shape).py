x, k = input().split()
x = int(x)

mid = x // 2

for i in range(x):
    row = []
    for j in range(x):
        if i == j or i + j == x - 1:
            if k == '#':
                row.append('#')
            else:
                # คำนวณระยะห่างจากจุดศูนย์กลาง
                dist = abs(i - mid)
                # ตรงกลางคือ k แล้วเพิ่มรหัส ASCII ขึ้นตามระยะห่าง
                char_code = ord(k) + dist
                row.append(chr(char_code))
        else:
            row.append('-')
    print("".join(row))
