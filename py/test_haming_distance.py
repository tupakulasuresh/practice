# haming distance is difference between 2 equal strings
def hamming_distance1(x, y):
    x = bin(x)[2:]
    y = bin(y)[2:]
    diff = len(x) - len(y)
    if diff > 0:
        y = "0" * diff + y
    elif diff < 0:
        x = "0" * abs(diff) + x

    return sum([1 if i != j else 0 for i, j in zip(x, y)])

def hamming_distance(x, y):
    x = "{0:b}".format(x)
    y = "{0:b}".format(y)
    diff = len(x) - len(y)
    if len(x) > len(y):
        y = y.zfill(len(x))
    else:
        x = x.zfill(len(y))
    distance = 0
    for i, j in zip(x, y):
        if i != j:
            distance += 1
    return distance

print hamming_distance(1, 4)
