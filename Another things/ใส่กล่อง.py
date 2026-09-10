W, L, M, N = map(int, input().split())
total_area = W * L
min_wasted = total_area
for A in range(M, N + 1):
    k1 = L // A         
    R = L % A          
    k2 = W // A        
    used_area = (W * k1 * A) + (R * k2 * A)
    wasted_area = total_area - used_area
    if wasted_area < min_wasted:
        min_wasted = wasted_area
    if min_wasted == 0:
        break
print(min_wasted)
