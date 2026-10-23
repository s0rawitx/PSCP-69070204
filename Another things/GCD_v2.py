'''dadad'''
def find_gcd(a, b):
    '''dada'''
    while b:
        a, b = b, a % b
    return a
NUM_ONE = int(float(input()))
NUM_TWO = int(float(input()))

print(find_gcd(NUM_ONE, NUM_TWO))
