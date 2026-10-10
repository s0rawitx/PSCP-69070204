yo = []
while True:
    line = input()
    if line == "DONE":
        break
    elif line == "CLOSED":
        yo = []
        break
    elif line == "SOMETHING'S WRONG":
        yo = []
    elif line.startswith("Can't do: "):
        dish = line.replace("Can't do: ", "").strip()
        if dish in yo:
            yo.remove(dish)
    else:
        if " #" in line:
            dish, pos = line.rsplit(" #", 1)
            if pos == "N":
                yo.append(dish)
            else:
                yo.insert(int(pos) - 1, dish)

reverse_yo = yo.copy()
reverse_yo.reverse()
print(f"Full Course: {yo} Reversed: {reverse_yo}")  