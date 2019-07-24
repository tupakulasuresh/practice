import unittest

# Defaults
DEBUG_ON_FAIL = False
STOP_AFTER_TEST_CASE = None
DEBUG_UTILITY = 'ipython'

# FIXME : remove these
DEBUG_ON_FAIL = True
STOP_AFTER_TEST_CASE = 'test4'
DEBUG_UTILITY = 'ipython'


class TestcaseDebug(unittest.TestResult):

    @staticmethod
    def get_testmethod_name(test):
        if test is not None:
            try:
                # to retrieve testcase name only
                test = test._testMethodName
            except Exception:
                pass
        return test

    @staticmethod
    def debug_required(test, status_failed=False):
        if TestcaseDebug.is_debug_eligible_test(test):
            print ("Requested debug mode after testcase=%s" %
                   TestcaseDebug.get_testmethod_name(test))
            return True
        elif (DEBUG_ON_FAIL and status_failed):
            print ("Testcase=%s failed. Requested for debug on failure" %
                   TestcaseDebug.get_testmethod_name(test))
            return True
        else:
            return False

    @staticmethod
    def is_debug_eligible_test(test):
        if STOP_AFTER_TEST_CASE == TestcaseDebug.get_testmethod_name(test):
            return True
        return False

    @staticmethod
    def start_ipython_debug():
        from IPython import embed
        embed()

    @staticmethod
    def start_pdb():
        from pdb import set_trace
        set_trace()

    @staticmethod
    def start_debug(test=None):
        print (">>>>>>>> Dropping to interactive prompt >>>>>>>>>>")
        if DEBUG_UTILITY == 'pdb':
            TestcaseDebug.start_pdb()
        else:
            TestcaseDebug.start_ipython_debug()

    def addSuccess(self, test):
        if TestcaseDebug.debug_required(test, status_failed=False):
            TestcaseDebug.start_debug(test)

        super(TestcaseDebug, self).addSuccess(test)

    def addFailure(self, test, err):
        if TestcaseDebug.debug_required(test, status_failed=True):
            TestcaseDebug.start_debug(test)
        super(TestcaseDebug, self).addFailure(test, err)
