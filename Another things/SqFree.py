'''fsfs'''
def is_square_free(x):
    '''dadadad'''
    b = 2
    while b * b <= x:
        if not x % (b * b):
            return False
        b += 1
    return True
def main():
    '''dadad'''
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if is_square_free(i):
            count += 1
    print(count)
main()
