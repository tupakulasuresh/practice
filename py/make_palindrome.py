"""
Dummy test
"""
import sys
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(filename)s:%(lineno)d %(message)s',
                    datefmt='%T')
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.setLevel(logging.INFO)


def make_palindrome(str1):
    '''
    function to make a string as palindrome
    '''

    # to indicate the position of comparision. to ignore already compared elements
    start = 0
    # for better comparision
    str1 = str1.lower()
    origin_str = str1[:]
    while str1:
        str_len = len(str1)
        for i in range(start, str_len / 2):
            j = 0 - i - 1
            start = i
            if str1[i] != str1[j]:
                LOG.debug("i=%d, j=%d, '%c' != '%c'", i, j, str1[i], str1[j])
                if i == 0:
                    str1 = str1[:j]
                else:
                    str1 = str1[:j] + str1[j + 1:]
                LOG.debug("Modified string is %s", str1)
                break
            else:
                LOG.debug("i=%d, j=%d, '%c' == '%c'", i, j, str1[i], str1[j])
        else:
            break
    if not str1 or len(str1) == 1:
        LOG.warning("Can't make '%s' as palidrome", origin_str)
        str1 = None
    elif str1 == origin_str:
        LOG.info("Input '%s' is palindrome", origin_str)
    else:
        LOG.info("Modified '%s' to '%s' to make as palindrome", origin_str, str1)
    return str1


make_palindrome(sys.argv[1])
