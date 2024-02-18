from . import di


class Registry:
    @staticmethod
    def implements(*, interface):
        return di.implements(interface=interface)

    @property
    def data(self):
        return di.registry_data()

    def get(self, interface):
        return di.get(interface)
