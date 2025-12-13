B I G T A L K
=============


**NAME**


|
| ``bigtalk`` - Big Talk
|


**SYNOPSIS**

::

    >>> from bigtalk.objects import Object
    >>> from bigtalk.serials import Json
    >>> o = Object()
    >>> o.a = "b"
    >>> print(Json.loads(Json.dumps(o)))
    {'a': 'b'}


**DESCRIPTION**

BigTalk has all you need to program a unix cli program, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, etc.

BiGTalk contains python3 code to program objects in a functional
way. it provides an “clean namespace” Object class that only has
dunder methods, so the namespace is not cluttered with method names.
This makes storing and reading to/from json possible.


**INSTALL**

installation is done with pip

|
| ``$ pip install bigtalk``
|

**FILES**

|
| ``~/.bigtalk``
| ``~/.local/bin/bigtalk``
| ``~/.local/share/pipx/venvs/bigtalk/*``
|


**AUTHOR**

|
| Bart Thate <``bthate@dds.nl``>
|

**COPYRIGHT**

|
| ``BigTalk`` is Public Domain.
|
