n1 = input().split()
n2 = input().split()
xA = int(n1[0])
yA = int(n1[1])
wA = int(n1[2])
hA = int(n1[3])
xB = int(n2[0])
yB = int(n2[1])
wB = int(n2[2])
hB = int(n2[3])

LeftCornerA = xA
RightCornerA = xA + wA
lowerCornerA = yA
TopCornerA = yA + hA

LeftCornerB = xB
RightCornerB = xB + wB
lowerCornerB = yB
TopCornerB = yB + hB

overlap_left = max(LeftCornerA, LeftCornerB)
overlap_right = min(RightCornerA, RightCornerB)
overlap_width = overlap_right - overlap_left

overlap_lower = max(lowerCornerA, lowerCornerB)
overlap_top = min(TopCornerA, TopCornerB)
overlap_height = overlap_top - overlap_lower
if overlap_width <=0 or overlap_height <= 0:
    print("no overlapping")
else:
    print(overlap_width * overlap_height)
