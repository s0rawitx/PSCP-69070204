"""Module for solving the bread cutting problem."""
def solve_bread_cutting():
    """Solve the bread cutting problem and print the top two largest areas."""
    first_line = input().split()
    if not first_line:
        return
    w = int(first_line[0])
    h = int(first_line[1])
    x_inputs = [int(x) for x in input().split()]
    x_coords = [0] + x_inputs + [w]
    y_inputs = [int(y) for y in input().split()]
    y_coords = [0] + y_inputs + [h]
    widths = [
        x_coords[i] - x_coords[i - 1]
        for i in range(1, len(x_coords))
    ]
    heights = [
        y_coords[i] - y_coords[i - 1]
        for i in range(1, len(y_coords))
    ]
    areas = []
    for width in widths:
        for height in heights:
            areas.append(width * height)
    areas.sort(reverse=True)
    print(f"{areas[0]} {areas[1]}")
solve_bread_cutting()
