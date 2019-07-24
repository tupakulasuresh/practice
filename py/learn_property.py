import pdb


class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if hasattr(self, '_gender'):
            raise Exception('Gender can only be set during init')
        elif value in ['M', 'F', 'Male', 'Female']:
            self._gender = value
        else:
            raise ValueError('Invalid gender %s' % value)

    @gender.deleter
    def gender(self):
        raise Exception('Cannot delete attribute without destorying object')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError('Age should be Integer. Specified %s' % value)

    @age.deleter
    def age(self):
        raise Exception('Cannot delete attribute without destorying object')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception('Name can only be set during init')
        elif isinstance(value, int):
            raise ValueError('Name cannot be integer')
        else:
            self._name = value

    @name.deleter
    def name(self):
        raise Exception('Cannot delete attribute without destorying object')


class Celsius(object):

    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


p1 = Person('suresh', 40, 'M')
p2 = Person('abc', 50, 'M')


# p1.gender = '10'

pdb.set_trace()
