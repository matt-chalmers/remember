
from ..remember.memory import recall, forget, memorise, Memory


_ID = 0
def _gen_id():
    global _ID
    _ID += 1
    return _ID


def test_type_of_recall():
    memory = recall('qwerty_%s' % _gen_id())
    assert isinstance(memory, Memory)


def test_recall_empty():
    memory = recall('qwerty_%s' % _gen_id())
    assert memory == None


def test_set_and_recall():
    key = 'qwerty_%s' % _gen_id()
    memorise(key, 42)
    memory = recall(key)
    assert (memory == 42)


def test_set_and_change():
    key = 'qwerty_%s' % _gen_id()
    memorise(key, 41)
    memorise(key, 42)
    memory = recall(key)
    assert (memory == 42)


def test_set_and_forget():
    key = 'qwerty_%s' % _gen_id()
    memorise(key, 42)
    forget(key)
    memory = recall(key)
    assert (memory == None)
