def is_prime(n):
    i = 2 
    if n == 2:
        return False
    while ( i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def generate_prime(n):
    for i in xrange(2, n+1):
        if is_prime(i):
            yield i
n = 10000000000
n = 15
for i in generate_prime(n):
    print i
