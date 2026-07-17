pushup=int(input())
situp=int(input())
squat=int(input())
run=int(input())
one_d_pushup=int(input())
one_d_situp=int(input())
one_d_run=int(input())
one_d_squat=int(input())
day=[]
#วิดพื้น
if pushup % one_d_pushup != 0:
    day.append((pushup // one_d_pushup)+1)
else:
    day.append(pushup // one_d_pushup)
#ซิทอัพ
if situp % one_d_situp != 0:
    day.append((situp // one_d_situp)+1)
else:
    day.append(situp // one_d_situp)
#ลุกนั่ง
if squat % one_d_squat != 0:
    day.append((squat//one_d_squat)+1)
else:
    day.append(squat//one_d_squat)
#วิ่ง
if run % one_d_run != 0:
    day.append((run // one_d_run)+1)
else:
    day.append(run//one_d_run)
day.sort(reverse=True)
print(day[0])
