
from abc import ABCMeta, abstractproperty


class Memory(object):

    __metaclass__ = ABCMeta

    @abstractproperty
    def value(self):
        return None

    def __eq__(self, other):
        other = other.value if isinstance(other, Memory) else other
        return self.value == other


class SimpleMemory(Memory):

    _MEMORIES = {}

    def __init__(self, key):
        self.key = key

    @property
    def value(self):
        return self._MEMORIES.get(self.key)

    @value.setter
    def value(self, value):
        if value is None:
            del self._MEMORIES[self.key]
        else:
            self._value = self._MEMORIES[self.key] = value


def recall(key):
    return SimpleMemory(key)
