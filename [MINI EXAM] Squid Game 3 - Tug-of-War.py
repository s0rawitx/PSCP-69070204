A=[int(input()) for _ in range(10)]
B=[int(input()) for _ in range(10)]
if sum(A) > sum(B):
    print("B")
elif sum(B) > sum(A):
    print("A")
else:
    print("AB")
