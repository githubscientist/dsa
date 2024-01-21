# iterative way
def gcd(m, n):
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


print(gcd(12, 16))
