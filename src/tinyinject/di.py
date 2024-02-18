import functools as fn
from contextlib import contextmanager

_registry_data = {}


def registry_data():
    return _registry_data


def get(interface):
    maybe_type = _registry_data[interface]

    if isinstance(maybe_type, type):
        return maybe_type()

    return maybe_type


def implements(*, interface: type):
    def wrapper(implementation: type | object):
        _registry_data[interface] = implementation
        return implementation

    return wrapper


class Require:
    def __init__(self, interface):
        self._interface = interface

    def __get__(self, obj, objtype=None):
        return get(self._interface)


def require_kwargs(**deps):
    def decorator(func):
        @fn.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **(kwargs | {k: get(v) for k, v in deps.items()}))

        return wrapper

    return decorator


@contextmanager
def override(interface, *, using: type | object):
    previous = get(interface)
    implements(interface=interface)(using)
    yield
    implements(interface=interface)(previous)
