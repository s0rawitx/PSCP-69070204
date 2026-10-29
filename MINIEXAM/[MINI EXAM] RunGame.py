line = input().strip()
try:
    if not line:
        print(0)
    else:
        positions = [int(x) for x in line.split()]
        total_distance = abs(positions[0])

        for i in range(1, len(positions)):
            total_distance += abs(positions[i] - positions[i - 1])

        print(total_distance)
except EOFError:
    print("0")