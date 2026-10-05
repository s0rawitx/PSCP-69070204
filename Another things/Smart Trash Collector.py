n = int(input())
trash = [input() for _ in range(n)]

what = []
for u in trash:
    for l in u.split():
        what.append(l)
idx = 0
for _ in range(n):
    plastic = float(what[idx])
    can = float(what[idx + 1])
    glass = float(what[idx + 2])
    idx += 3 
    total = plastic + can + glass
    alerts = []
    if total > 50.0:
        alerts.append("Overloaded")
    if plastic > 20.0:
        alerts.append("Check Type Plastic")
    if can > 20.0:
        alerts.append("Check Type Can")
    if glass > 20.0:
        alerts.append("Check Type Glass")
    if alerts:
        print(f"{total:.1f}, {', '.join(alerts)}")
    else:
        print(f"{total:.1f}")
