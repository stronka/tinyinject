from typing import Protocol

from src.tinyinject.require import Require, require_kwargs
from src.tinyinject import di


class ExampleType(Protocol):
    pass


@di.implements(interface=ExampleType)
class ExampleImpl:
    pass


class TestRequireDescriptor:
    def test_always_return_from_the_registry(self):
        class Other:
            example: ExampleType = Require(ExampleType)

        assert isinstance(Other().example, ExampleImpl)


class TestRequireDecorator:
    def test_always_inject_from_registry(self):
        @require_kwargs(dependency=ExampleType)
        def some_function(*, dependency: ExampleType):
            return dependency

        assert isinstance(some_function(), ExampleImpl)
