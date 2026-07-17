price = int(input())
cap = int(input())
free = int(input())
money = int(input())

bought = money // price
total = bought
current_caps = bought

if cap == 0 or bought < cap:
    print(total)
else:
    while current_caps >= cap:
        new_free = (current_caps // cap) * free
        total += new_free
        current_caps = (current_caps % cap) + new_free
    print(total)