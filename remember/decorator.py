
import wrapt
import functools


def remember(wrapped=None):
    if wrapped is None:
        return functools.partial(remember)

    @wrapt.decorator
    def decorator(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)

    return decorator(wrapped)
