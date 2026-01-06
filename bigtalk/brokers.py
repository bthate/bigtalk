# This file is placed in the Public Domain.


"an object for a string"


class Brokers:

    objects = {}


class Broker:

    def add(obj):
        "add object to the broker, key is repr(obj)."
        Brokers.objects[repr(obj)] = obj

    def get(origin):
        "object by repr(obj)."
        return Brokers.objects.get(origin)

    def objs(attr):
        "object with a certain attribute."
        for obj in Brokers.objects.values():
            if attr in dir(obj):
                yield obj

    def like(txt):
        "all keys with a substring in their key."
        for orig in Brokers.objects:
            if orig.split()[0] in orig.split()[0]:
                yield orig


def __dir__():
    return (
        'Broker',
    )
