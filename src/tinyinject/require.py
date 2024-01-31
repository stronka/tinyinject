from src.tinyinject import Registry
import functools as fn

_registry = Registry()


class Require:
    def __init__(self, interface):
        self._interface = interface

    def __get__(self, obj, objtype=None):
        return _registry.get(self._interface)


def require_kwargs(**deps):
    def decorator(func):
        @fn.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **(kwargs | {k: _registry.get(v) for k, v in deps.items()}))

        return wrapper

    return decorator
