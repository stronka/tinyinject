from typing import Protocol

import pytest

from src.tinyinject.registry import Registry


class ExampleType(Protocol):
    """Test example"""


class ExampleCallable(Protocol):
    def __call__(self, *args, **kwargs) -> int:
        ...


class TestRegistry:
    @pytest.fixture
    def registry(self):
        return Registry()

    def test_implements_case_type_then_register_it(self, registry):
        @registry.implements(interface=ExampleType)
        class ExampleTypeImpl:
            pass

        assert registry.data[ExampleType] == ExampleTypeImpl

    def test_get_case_type_then_return_instance(self, registry):
        @registry.implements(interface=ExampleType)
        class ExampleTypeImpl:
            pass

        assert isinstance(registry.get(ExampleType), ExampleTypeImpl)

    def test_implements_case_callable_interface_then_can_use_function(self, registry):
        @registry.implements(interface=ExampleCallable)
        def callable_impl():
            return 42

        assert registry.get(ExampleCallable)() == 42

    def test_implements_case_callable_implemented_by_callable_then_behaves_as_function(self, registry):
        @registry.implements(interface=ExampleCallable)
        class Callable:
            def __call__(self, *args, **kwargs):
                return 42

        assert registry.get(ExampleCallable)() == 42
