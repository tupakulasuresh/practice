class LRU(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.order = list()

    def _move_front(self, key):
        self.order.remove(key)
        self.order.insert(0, key)

    def get(self, key):
        if key in self.order:
            self._move_front(key)
            self.print_current_order()
            return self.cache.get(key)
        else:
            return -1

    def put(self, key, val):
        if key in self.order:
            self._move_front(key)
        else:
            if len(self.order) == self.capacity:
                self.cache.pop(self.order.pop())
            self.order.insert(0, key)
        self.print_current_order()
        self.cache[key] = val

    def print_current_order(self):
        print "Current order: ", self.order
