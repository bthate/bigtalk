# This file is placed in the Public Domain.


from bigtalk.package import Mods


def mod(event):
    event.reply(Mods.list())
