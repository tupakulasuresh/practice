def abc1(my_arg1='1', **kwargs):
    print my_arg1


def abc2(my_arg2='2', **kwargs):
    print my_arg2


def abc3(my_arg2='3', **kwargs):
    print my_arg2


kwargs = {'my_arg1': 4, 'my_arg4': 3}

abc1(**kwargs)
abc2(**kwargs)
abc3(**kwargs)
