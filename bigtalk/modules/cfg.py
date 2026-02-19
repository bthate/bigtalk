# This file is placed in the Public Domain.


"configuration"


from bigtalk.command import Cfg
from bigtalk.objects import Dict, Methods
from bigtalk.package import Mods
from bigtalk.persist import Disk, Locate


def cfg(event):
    cfg = None
    mod = None
    name = ""
    if event.args:
        name = event.args[0]
    if not name:
        cfg = Cfg
    if not cfg:
        modlist = list(Mods.get(name))
        if modlist:
            mod = modlist[0][-1]
            cfg = getattr(mod, "Cfg", None) 
        if not cfg:
            event.reply(f"{name} has no configuration.")
            return
    if not event.sets:
        event.reply(
            Methods.fmt(
                cfg,
                Dict.keys(cfg),
                skip=["password",]
            )
        )
        return
    fnm = Locate.last(cfg or Methods.ident(cfg)) 
    Methods.edit(cfg, event.sets)
    Disk.write(cfg, fnm)
    event.reply("ok")
