
def sqrt(n, min=1, max=None):
    if max is None:
        max = n
    if max < min:
        return -1
    guess = ( max + min ) / 2
    square = guess * guess
    if square == n:
        return guess
    if square < n:
        min = guess + 1
    else:
        max = guess - 1 
    return sqrt(n, min, max)

print sqrt(4)
print sqrt(3)


