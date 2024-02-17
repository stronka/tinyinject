_registry_data = {}


class Registry:
    @staticmethod
    def implements(*, interface: type):
        def wrapper(implementation: type | object):
            _registry_data[interface] = implementation
            return implementation

        return wrapper

    @property
    def data(self):
        return _registry_data

    def get(self, interface):
        maybe_type = _registry_data[interface]

        if isinstance(maybe_type, type):
            return maybe_type()

        return maybe_type


di = Registry()
