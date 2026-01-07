# This file is placed in the Public Domain.


"persistence through storage"


import json
import threading


from .objects import update
from .serials import dump, load
from .utility import cdir
from .workdir import getpath


lock = threading.RLock()


class Cache:

    objects = {}

    @staticmethod
    def add(path, obj):
        "put object into cache."
        Cache.objects[path] = obj

    @staticmethod
    def get(path):
        "get object from cache."
        return Cache.objects.get(path, None)

    @staticmethod
    def sync(path, obj):
        "update cached object."
        try:
            update(Cache.objects[path], obj)
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
