'''ink'''
import math
speedandhouse=input().split()
t=[]
for _ in range(int(speedandhouse[1])):
    xy=input().split()
    area=3.1416*((int(xy[0])**2)+(int(xy[1])**2))
    time=math.ceil(area/int(speedandhouse[0]))
    t.append(time)
print(*t,sep='\n')
