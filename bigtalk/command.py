# This file is placed in the Public Domain.


"write your commands"


import inspect


from .brokers import Broker
from .methods import parse


class Commands:

    cmds = {}
    names = {}


class Command:

    def add(*args):
        "add functions to commands."
        for func in args:
            name = func.__name__
            Commands.cmds[name] = func
            Commands.names[name] = func.__module__.split(".")[-1]

    def get(cmd):
        "command by string."
        return Commands.cmds.get(cmd, None)


def command(evt):
    "command callback."
    parse(evt, evt.text)
    func = Command.get(evt.cmd)
    if func:
        func(evt)
        bot = Broker.get(evt.orig)
        bot.display(evt)
    evt.ready()



def scan(module):
    "scan a module for functions with event as first argument."
    for key, cmdz in inspect.getmembers(module, inspect.isfunction):
        if 'event' not in inspect.signature(cmdz).parameters:
            continue
        Command.add(cmdz)


def __dir__():
    return (
        'Commands',
        'Command',
        'command',
        'scan'
    )
