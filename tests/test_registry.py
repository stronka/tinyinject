from typing import Protocol
from src.tinyinject import di


class ExampleType(Protocol):
    """Test example"""


class ExampleCallable(Protocol):
    def __call__(self, *args, **kwargs) -> int:
        ...


class TestRegistry:
    def test_implements_case_type_then_register_it(self):
        @di.implements(interface=ExampleType)
        class ExampleTypeImpl:
            pass

        assert di.registry_data()[ExampleType] == ExampleTypeImpl

    def test_get_case_type_then_return_instance(self):
        @di.implements(interface=ExampleType)
        class ExampleTypeImpl:
            pass

        assert isinstance(di.get(ExampleType), ExampleTypeImpl)

    def test_implements_case_callable_interface_then_can_use_function(self):
        @di.implements(interface=ExampleCallable)
        def callable_impl():
            return 42

        assert di.get(ExampleCallable)() == 42

    def test_implements_case_callable_implemented_by_callable_then_behaves_as_function(self):
        @di.implements(interface=ExampleCallable)
        class Callable:
            def __call__(self, *args, **kwargs):
                return 42

        assert di.get(ExampleCallable)() == 42
