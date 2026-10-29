'''dadad'''
def main():
    '''dadad'''
    day = int(input())
    month = int(input())
    year = int(input())

    deadline_day = 2
    deadline_month = 10
    deadline_year = 2569

    deadline_total = deadline_year * 360 + (deadline_month - 1) * 30 + deadline_day
    input_total = year * 360 + (month - 1) * 30 + day

    remaining_days = deadline_total - input_total

    if remaining_days < 0:
        print(0)
    else:
        print(remaining_days)
main()
