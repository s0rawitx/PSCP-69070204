s = input().strip().upper()
n = len(s)

state = 0   # 0 = ปกติ, 1 = เพิ่งเจอ R (ต้องตามด้วย A), 2 = อยู่ใน A ที่ตามหลัง R, 3 = เพิ่งเจอ B (ต้องตามด้วย I/T)
bad = -1

for i, c in enumerate(s):
    if state == 2 and c != 'A':
        state = 0                      # จบช่วง A แล้ว ประมวลผลตัวนี้เหมือนสถานะปกติ

    if state == 0:
        if c == 'R':
            state = 1
        elif c == 'B':
            state = 3
        elif c in 'IT':
            pass
        else:                          # A โดดๆ ที่ไม่ได้ตามหลัง R
            bad = i
            break
    elif state == 1:
        if c == 'A':
            state = 2
        else:
            bad = i
            break
    elif state == 2:                   # c == 'A'
        pass
    elif state == 3:
        if c in 'IT':
            state = 0
        else:
            bad = i
            break

# จบสตริงแล้วยังรอ A หลัง R หรือ I/T หลัง B
if bad == -1 and state in (1, 3):
    bad = n

if bad != -1:
    print("no", bad)
elif all(c in 'IT' for c in s):
    print("unknown", n)
else:
    best = cur = 0
    for c in s:
        if c == 'A':
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    print("yes", best)