def list_sum_zero(n):
    res = []
    if n % 2 == 1:
        res = [0]
        n -= 1
    while n:
        res += [n, -n]
        n -= 2
    return res

print list_sum_zero(8)
