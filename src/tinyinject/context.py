from contextlib import contextmanager
from src.tinyinject import Registry

_registry = Registry()


@contextmanager
def override(interface, *, using: type | object):
    previous = _registry.get(interface)
    _registry.implements(interface=interface)(using)
    yield
    _registry.implements(interface=interface)(previous)
