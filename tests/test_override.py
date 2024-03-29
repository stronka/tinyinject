from typing import Protocol

from src.tinyinject import di
from src.tinyinject import override
from src.tinyinject import Require
from src.tinyinject import require_kwargs


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
