def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True


def permutations(s):
    def _permutations(s, prefix=''):
        if not s:
            print prefix
        else:
            for i in range(len(s)):
                _permutations(s[:i] + s[i+1:], prefix + s[i])
    _permutations(s)


def Fib(n):
    tmp_arr = [0, 1]

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def generate_fib(n):
    fib_list = [None] * n

    def _fib(n):
        if n <= 0:
            val = 0
            n = 0
        elif n == 1:
            val = 1
        elif fib_list[n]:
            val =  fib_list[n]
        else:
            val = _fib(n-2) + _fib(n-1)
        fib_list[n] = val
        return val
    for i in range(n):
        _fib(i)
    return fib_list


def powerX(n, x):
    # x*x till n
    if n == 1:
        print n
        return 1
    else:
        prev = powerX(n / x, x)
        curr = prev * x
        print curr
        return curr

def power(a, b):
    # a power b
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b -1)

print power(3, 5)
