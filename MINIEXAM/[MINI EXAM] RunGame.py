run=input().split()
result=0
for number in run:
    result+=int(number)
re_run=result-int(run[-1])
print(re_run)
print(result-re_run)
