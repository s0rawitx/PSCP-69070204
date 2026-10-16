'''adadadad'''
def solve():
    """Solve the bowl stacking problem."""
    with open(0, "r", encoding="utf-8") as f:
        input_data = f.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    count = [0] * 301
    for i in range(1, n + 1):
        size = int(input_data[i])
        count[size] += 1
    print(max(count))
solve()
