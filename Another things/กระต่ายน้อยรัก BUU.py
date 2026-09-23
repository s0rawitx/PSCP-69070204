# รับข้อมูลข้อความ
original_s = input().strip()
s = original_s.upper()
n = len(s)
max_u = 0
for i in range(n):
    if s[i] == 'B':
        u_count = 0
        j = i + 1
        while j < n and s[j] == 'U':
            u_count += 1
            j += 1
        if u_count >= 2:
            if u_count > max_u:
                max_u = u_count
if max_u >= 2:
    print(f"Yes {max_u}")
else:
    b_pos = s.find('B')
    if b_pos != -1:
        # มี B แต่ไม่มี BUU -> เปลี่ยนหลัง B ตัวแรกเป็น U ทั้งหมด
        ans = original_s[:b_pos + 1] + ('U' * (n - b_pos - 1))
        print(ans)
    else:
        # ไม่มี B เลย -> วนพิมพ์ BUU จนเท่าความยาวเดิม
        pattern = "BUU"
        ans = "".join(pattern[i % 3] for i in range(n))
        print(ans)