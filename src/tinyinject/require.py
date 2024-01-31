from .registry import di
import functools as fn


class Require:
    def __init__(self, interface):
        self._interface = interface

    def __get__(self, obj, objtype=None):
        return di.get(self._interface)


def require_kwargs(**deps):
    def decorator(func):
        @fn.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **(kwargs | {k: di.get(v) for k, v in deps.items()}))

        return wrapper

    return decorator
