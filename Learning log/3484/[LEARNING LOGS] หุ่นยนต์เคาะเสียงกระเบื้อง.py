'''dada'''
n, p = input().split()
n = int(n)
p = float(p)

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

row_tile_counts = []
row_point_counts = []

for row in grid:
    tile_count = 0
    point_count = 0
    for val in row:
        if val > 0:
            tile_count += 1
            point_count += val
    row_tile_counts.append(tile_count)
    row_point_counts.append(point_count)

col_tile_counts = [0] * n
col_point_counts = [0] * n

for c in range(n):
    t_count = 0
    p_count = 0
    for r in range(n):
        val = grid[r][c]
        if val > 0:
            t_count += 1
            p_count += val
    col_tile_counts[c] = t_count
    col_point_counts[c] = p_count

for i in range(n):
    row_str = " ".join(map(str, grid[i]))
    print(f"{row_str} {row_tile_counts[i]} {row_point_counts[i]}")

print(" ".join(map(str, col_tile_counts)))
print(" ".join(map(str, col_point_counts)))

total_tiles = sum(row_tile_counts)
total_points = sum(row_point_counts)
total_fine = total_points * p

print(f"{total_tiles} {total_points} {total_fine:.2f}")
