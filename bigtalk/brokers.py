# This file is placed in the Public Domain.


"an object for a string"


class Broker:

    objs = {}

    @staticmethod
    def add(obj):
        "add object to the broker, key is repr(obj)."
        Broker.objs[repr(obj)] = obj

    @staticmethod
    def get(origin):
        "object by repr(obj)."
        return Broker.objs.get(origin)

    @staticmethod
    def getobjs(attr):
        "objects with a certain attribute."
        for obj in Broker.objs.values():
            if attr in dir(obj):
                yield obj

    @staticmethod
    def has(obj):
        "whether the Broker has object."
        return repr(obj) in Broker.objs

    @staticmethod
    def like(txt):
        "all keys with a substring in their key."
        for orig in Broker.objs:
            if txt in orig.split()[0]:
                yield orig


"interface"


def __dir__():
    return (
        'Broker',
    )
