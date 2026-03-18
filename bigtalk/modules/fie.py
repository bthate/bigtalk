# This file is placed in the Public Domain.


"show fields on objects"


from bigtalk.persist import Locate, Workdir


def fie(event):
    if not event.rest:
        res = sorted({y.split('.')[-1].lower() for y in Workdir.kinds()})
        if res:
            event.reply(",".join(res))
        else:
            event.reply("no kinds")
        return
    fields = Locate.attrs(event.args[0])
    if not fields:
        event.reply("no fields")
    else:
        event.reply(",".join(fields))
