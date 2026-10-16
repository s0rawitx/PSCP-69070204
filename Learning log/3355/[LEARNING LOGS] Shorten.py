'''adada'''
numbers = []
while True:
    try:
        n = int(input())
        if n == -1:
            break
        numbers.append(n)
    except EOFError:
        break
if numbers:
    ranges = []
    start = numbers[0]
    end = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = numbers[i]
            end = numbers[i]
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")
    print(", ".join(ranges))
