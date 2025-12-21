# This file is placed in the Public Domain.


from bigtalk.classes import Mods


def mod(event):
    event.reply(Mods.list())
