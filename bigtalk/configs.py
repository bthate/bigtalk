# This file is placed in the Public Domain.


"configuration"


from .locater import last
from .objects import Default
from .utility import where


class Config(Default):

    pass


Cfg = Config()
Cfg.name = Config.__module__.split(".")[0]


def __dir__():
    return (
        'Cfg',
    )
