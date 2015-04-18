__author__ = 'Margherita'


class NotAllowError(Exception):
    pass


class Event(object):

    def add_observer(self, observer):
        raise NotImplementedError

    def get_observers(self):
        raise NotImplementedError

    def fire(self, *args):
        for observer in self.get_observers():
            observer(*args)


class EventImmutable(Event):

    def __init__(self, *observers):
        self.observers = tuple(*observers)

    def add_observer(self, observer):
        raise NotAllowError

    def get_observers(self):
        return self.observers


class EventMutable(Event):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def get_observers(self):
        return self.observers