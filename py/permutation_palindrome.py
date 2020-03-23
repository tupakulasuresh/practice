from collections import Counter

def is_palindrome(str1):
    str1 = str1.replace(" ", "").strip()
    if not str1:
        return False

    c1 = Counter(str1)
    # get odd items
    odd_count_items = [item for item in c1.iteritems() if item[1] % 2 != 0]
    print odd_count_items
    if not odd_count_items or len(odd_count_items) == 1:
        return True
    else:
        return False



print is_palindrome("go go")
print is_palindrome("malayalam  gooy")
print is_palindrome("tact cao")
print is_palindrome("mbadm")
