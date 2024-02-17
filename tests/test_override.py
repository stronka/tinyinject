from typing import Protocol
from src.tinyinject import di, Require, require_kwargs
from src.tinyinject.context import override


class ExampleType(Protocol):
    ...


@di.implements(interface=ExampleType)
class ExampleTypeImpl:
    ...


class AnotherType:
    ...


class TestOverride:
    def test_case_descriptor_approach_replace_implementation_with_provided_one(self):
        with override(ExampleType, using=AnotherType):

            class Other:
                dependency: ExampleType = Require(ExampleType)

            assert isinstance(Other().dependency, AnotherType)

    def test_case_descriptor_after_exit_then_back_to_original_type(self):
        with override(ExampleType, using=AnotherType):

            class Other:
                dependency: ExampleType = Require(ExampleType)

        assert isinstance(Other().dependency, ExampleTypeImpl)

    def test_case_decorator_then_replace_implementation_with_provided_one(self):
        with override(ExampleType, using=AnotherType):

            @require_kwargs(dependency=ExampleType)
            def func(*, dependency):
                return dependency

            assert isinstance(func(), AnotherType)

    def test_case_decorator_after_exit_then_replace_implementation_with_original_one(self):
        with override(ExampleType, using=AnotherType):

            @require_kwargs(dependency=ExampleType)
            def func(*, dependency):
                return dependency

        assert isinstance(func(), ExampleTypeImpl)
