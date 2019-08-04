from operator import attrgetter


def sort_by_attribute(items, attr):
    return sorted(items, key=attrgetter(attr))


def sort_by_id(items):
    return sort_by_attribute(items, 'id')
