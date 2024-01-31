# tinyinject
A minimalistic protocol driven dependency injection framework for python.

## Installation

```commandline
python -m pip install tinyinject
```

## Examples

### Registering implementation to the DI registry

```python
# protocols.py
from typing import Protocol


class Arithmetic(Protocol):
    def sum(self, a: int, b: int) -> int:
        ...
    

# providers.py
from tinyinject import di
from .protocols import Arithmetic


@di.implements(interface=Arithmetic)
class _ArithmeticImplementation:
    def sum(self, a: int, b: int) -> int:
        return a + b
```

### Requesting dependencies via `Request` descriptor
```python
# main.py
from tinyinject import Request
from .protocols import Arithmetic


class App:
    _dependency: Arthmetic = Request(Arithmetic)
    
    def format_sum(self, a: int, b: int):
        print(f"Sum of {a} and {b} is {self._dependency.sum(a, b)}")
```


### Requesting dependencies via `request_kwargs` decorator
```python
# main.py
from tinyinject import request_kwargs
from .protocols import Arithmetic


@inject_kwargs(dependency=Arithmetic)
def format_sum(self, a: int, b: int, *, dependency: Arithmetic):
    print(f"Sum of {a} and {b} is {dependency.sum(a, b)}")
```


### Dependency Injection of functions
```python
# protocols.py
from typing import Protocol


class Sum(Protocol):
    def __call__(self, a: int, b: int) -> int:
        ...
    
    
# providers.py
from tinyinject import di
from .protocols import Sum


@di.implements(interface=Sum)
def sum_func(a: int, b: int) -> int:
    return a + b


# main.py
from tinyinject import Request
from .protocols import Sum


class App:
    _sum: Sum = Request(Sum)
    
    def format_sum(self, a: int, b: int) -> int:
        print(f"Sum of {a} and {b} is {self._sum(a, b)}")

```


### Using `override` context manager
This is written with testing in mind, however it will work in any use case where temporary replacement
of the provider is necessary.

```python
# test_sum.py
from unittest import mock
from protocols import Arithmetic
from tinyinject import override
from main import App



class TestSum:
    def test_app_format_sum_always_call_sum_with_correct_parameters(self):
        spy = mock.MagicMock()
        
        with override(Arithmetic, using=spy):
            App().format_sum(1, 2)
            
        spy.sum.assert_called_with(1, 2)
```