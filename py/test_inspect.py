import inspect


class Test1():

    @staticmethod
    def echo(message):
        print inspect.getframeinfo(inspect.currentframe())
        print message


class Test2():

    def echo(self):
        Test1.echo("Test2")


class Test3():

    def echo(self):
        Test1.echo("Test3")


t2 = Test2()
t2.echo()
