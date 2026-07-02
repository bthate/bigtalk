# This file is placed in the Public Domain.


"show path to website"


import os


d = os.path.dirname
e = os.path.exists
j = os.path.join


def pth(event):
    "create and show path to website."
    path = j(d(d(__file__)), "mirrors")
    if not event.args:
        event.iface(f'{",".join([x for x in os.listdir(path) if not x.startswith("__")])}')
        return
    name = event.args[0]
    path = j(path, name, "html", "index.html")
    if e(path):
        event.reply(f"file://{path}")
    else:
        event.reply("no index.html")
