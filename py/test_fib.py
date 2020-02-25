def fib(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def generate_fib(n):
    for i in range(0, n):
        print fib(i),
    print ""

# generate_fib(10)


# memoization

def mfib(n, memo):
    if n <= 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = mfib(n-1, memo) + mfib(n-2, memo)
    return memo[n]

def generate_mfib(n):
    memo = [None] * n
    for i in range(0, n):
        mfib(i, memo)
    print memo

# generate_mfib(10)

def powerOf2(n):
    if n < 0:
        return 0
    elif n < 2:
        curr = 1
    else:
        prev = powerOf2(n/2)
        curr = prev * 2
    print curr,
    return curr

def powerOf3(n):
    if n < 0:
        return 0
    elif n < 3:
        curr = 1
    else:
        prev = powerOf3(n/3)
        curr = prev * 3 
    print curr,
    return curr

powerOf3(234)
print
powerOf2(234)
