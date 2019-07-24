import traceback


def get_stack(stack_level=0):
    stack = traceback.extract_stack()
    # by default, caller information will be in the stack below this call
    stack_level += -2
    try:
        return stack[stack_level]
    except IndexError:
        return ["", "", "pygash", ""]


def get_calling_method():
    return get_stack(stack_level=-2)[-2]


def get_my_name():
    return get_stack(stack_level=-1)[-2]


def include_stack_info(msg, stack_level=0):
    (filename, codeline, funcName, _) = get_stack(stack_level - 1)
    return "{} | {}:{} | {}".format(funcName, filename, codeline, msg)


class junk(object):

    def my_log(self, msg):
        print include_stack_info(msg, stack_level=-1)


class bunk(object):

    def __init__(self):
        self.junk = junk()

    def bunk_log(self, msg):
        self.junk.my_log(msg)


b = bunk()
b.bunk_log("This is test")
print get_calling_method()
print get_my_name()
