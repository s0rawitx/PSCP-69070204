'''Ssa'''
n = int(input())
heavy_tasks = 0
light_tasks = 0
for _ in range(n):
    h = int(input())
    if h > 18:
        heavy_tasks += 1
    else:
        light_tasks += 1
if not heavy_tasks:
    print(n)
else:
    total_days = heavy_tasks + max(heavy_tasks - 1, light_tasks)
    print(total_days)
