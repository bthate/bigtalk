# This file is placed in the Public Domain.


"fields"


from bigtalk.locater import Locater
from bigtalk.workdir import Workdir


def atr(event):
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in Workdir.types()])
        if res:
            event.reply(",".join(res))
        else:
            event.reply("no types")
        return
    items = Locater.attrs(event.args[0])
    if not items:
        event.reply("no fields")
    else:
        event.reply(",".join(items))
