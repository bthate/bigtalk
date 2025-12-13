# This file is placed in the Public Domain.


"in the beginning"


import time


from .command import Commands
from .loggers import Logging
from .objects import Default
from .package import Mods
from .threads import Threads
from .utility import Utils
from .workdir import Workdir


class Kernel:

    @staticmethod
    def forever():
        while True:
            try:
                time.sleep(0.1)
            except (KeyboardInterrupt, EOFError):
                break

    @staticmethod
    def init(names, wait=False):
        mods = []
        thrs = []
        for name in Utils.spl(names):
            mod = Mods.get(name)
            if "init" not in dir(mod):
                continue
            thrs.append(Threads.launch(mod.init))
            mods.append(name)
        if wait:
            for thr in thrs:
                thr.join()
        return mods

    @staticmethod
    def scanner(names):
        for mod in Mods.mods(names):
            Commands.scan(mod)


def __dir__():
    return (
        'Kernel'
    )
