n = int(input())
over_count = 0
peak_val = -1
max_streak = 0
best_start = 0
current_streak = 0
current_start = 0
for day in range(1, n + 1):
    val = int(input())
    if val > peak_val:
        peak_val = val
    if val > 50:
        over_count += 1
        if current_streak == 0:
            current_start = day
        current_streak += 1
        if current_streak >= max_streak:
            max_streak = current_streak
            best_start = current_start
    else:
        current_streak = 0
        current_start = 0
print("OVER =", over_count)
print("PEAK =", peak_val)
print("STREAK =", max_streak)
print("START =", best_start)
