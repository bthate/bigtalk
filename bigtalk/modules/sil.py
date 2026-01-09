# This file is placed in the Public Domain.


from bigtalk.brokers import getobj


def sil(event):
    bot = gebigtalkj(event.orig)
    bot.silent = True
    event.reply("ok")


def lou(event):
    bot = gebigtalkj(event.orig)
    bot.silent = False
    event.reply("ok")
