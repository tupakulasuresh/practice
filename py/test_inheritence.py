class Parent(object):

    def __init__(self, x, y, z):
        print "INITIALIZING PARENT"
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "%s(%r, %r, %r)" % (self.__class__.__name__, self.x, self.y, self.z)

    def abc(self):
        print "abc"
        pass


class Child(Parent):

    _sentinel = object()

    def __init__(self, x, y=_sentinel, z=_sentinel):
        print "INITIALIZING CHILD"
        if y is self._sentinel and z is self._sentinel:
            print "HIJACKING"
            z = x.z
            y = x.y
            x = x.x
        Parent.__init__(self, x, y, z)
        print "CHILD IS DONE!"


p0 = Parent(1, 2, 3)
print p0
c1 = Child(p0)
print c1
c2 = Child(4, 5, 6)
print c2
