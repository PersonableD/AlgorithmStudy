import sys
input = sys.stdin.readline

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = [False] * len(range(p * p, limit + 1, p))
    primes = [i for i in range(limit + 1) if is_prime[i]]
    return is_prime, primes

MAX_N = 1000000
is_prime, primes = sieve(MAX_N)

while True:
    n = int(input())
    if n == 0:
        break
    ok = False
    for a in primes:
        if a > n // 2:
            break
        b = n - a
        if is_prime[b]:
            print(f"{n} = {a} + {b}")
            ok = True
            break
    if not ok:
        print("Goldbach's conjecture is wrong.")
