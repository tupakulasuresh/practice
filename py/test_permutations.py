
def permutations(str1, prefix=""):
    if len(str1) == 0:
        print prefix
    else:
        for i in range(len(str1)):
            remaining = str1[0:i] + str1[i+1:]
            permutations(remaining, prefix + str1[i])

permutations('abc')
        
