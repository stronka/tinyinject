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
