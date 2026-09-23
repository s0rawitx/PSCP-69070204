def right(n):
    total_rows = 2 * n - 1
    for i in range(total_rows):
        if i < n:
            stars = n - i
        else:
            stars = i - n + 2
        spaces = 2 * (n - stars)
        print(" " * spaces + "*" * stars)
def left(n):
    total_rows = 2 * n - 1
    for i in range(total_rows):
        if i < n:
            stars = n - i
        else:
            stars = i - n + 2
        spaces = stars - 1
        print(" " * spaces + "*" * stars)
def main():
    directions = input().strip()
    n = int(input().strip())

    for idx, d in enumerate(directions):
        if idx > 0:
            print()  
        if d == "R":
            right(n)
        elif d == "L":
            left(n)
main()
