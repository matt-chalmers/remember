
from ..remember.memory import recall, forget, Memory


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

    memory = recall(key)
    memory.value = 42

    memory2 = recall(key)
    assert (memory2 == 42)


def test_set_and_change():
    key = 'qwerty_%s' % _gen_id()

    memory = recall(key)
    memory.value = 41

    memory2 = recall(key)
    memory2.value = 42

    memory3 = recall(key)
    assert (memory3 == 42)


def test_set_and_forget():
    key = 'qwerty_%s' % _gen_id()

    memory = recall(key)
    memory.value = 42

    forget(key)

    memory2 = recall(key)
    assert (memory2 == None)
