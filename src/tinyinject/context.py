from contextlib import contextmanager
from src.tinyinject.registry import di


@contextmanager
def override(interface, *, using: type | object):
    previous = di.get(interface)
    di.implements(interface=interface)(using)
    yield
    di.implements(interface=interface)(previous)
