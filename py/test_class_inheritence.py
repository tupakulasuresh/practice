class Test1(object):
    scale = 100

    def test_1(self):
        print self.__class__, self.scale


class Test2(Test1):
    scale = 200


class Test3(Test1):
    pass


Test1.scale = 1000
Test2().test_1()
Test3().test_1()
