# This file is placed in the Public Domain.


"persistence through storage"


import json
import threading


from .objects import update
from .serials import dump, load
from .utility import cdir
from .workdir import getpath


lock = threading.RLock()


class Caches:

    objects = {}


class Cache:

    def add(path, obj):
        "put object into cache."
        Caches.objects[path] = obj

    def get(path):
        "get object from cache."
        return Caches.objects.get(path, None)

    def sync(path, obj):
        "update cached object."
        try:
            update(Caches.objects[path], obj)
        except KeyError:
            Cache.add(path, obj)


def read(obj, path):
    "read object from path."
    with lock:
        with open(path, "r", encoding="utf-8") as fpt:
            try:
                update(obj, load(fpt))
            except json.decoder.JSONDecodeError as ex:
                ex.add_note(path)
                raise ex


def write(obj, path=""):
    "write object to disk."
    with lock:
        if path == "":
            path = getpath(obj)
        cdir(path)
        with open(path, "w", encoding="utf-8") as fpt:
            dump(obj, fpt, indent=4)
        Cache.sync(path, obj)
        return path


def __dir__():
    return (
        'Cache',
        'read',
        'write'
    )
