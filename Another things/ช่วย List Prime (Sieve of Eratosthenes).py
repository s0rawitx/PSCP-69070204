'''dadad'''
def sieve_of_eratosthenes(limit):
    '''dadad'''
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    return is_prime


def main():
    '''dadadad'''
    n = int(input())

    if n <= 0 or n >= 32768:
        return

    primes = sieve_of_eratosthenes(n)

    if primes[n]:
        print("Yes")
        prime_list = [str(i) for i in range(2, n + 1) if primes[i]]
        print(" ".join(prime_list))
    else:
        print("No")


main()
