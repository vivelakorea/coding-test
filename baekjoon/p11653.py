import sys

def p11653(n):
    divider = 2
    prime_factors = []
    while n != 1:
        while n % divider == 0:
            prime_factors.append(divider)
            n //= divider
        divider += 1
    return prime_factors

N = int(sys.stdin.readline())
for prime_factor in p11653(N):
    print(prime_factor)
