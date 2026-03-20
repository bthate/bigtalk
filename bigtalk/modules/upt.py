# This file is placed in the Public Domain.


"show uptime"


import time


from bigtalk.utility import Time


STARTTIME = time.time()


def upt(event):
    event.reply(Time.elapsed(time.time()-STARTTIME))
