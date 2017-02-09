#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from os.path import abspath, dirname, join

from pyload.remote import apitypes
from pyload.remote.apitypes_debug import enums

path = dirname(abspath(__file__))
module = join(path, "..")


# generate js enums


def main():

    print("generating apitypes.js")

    with open(join(module, 'webui', 'app', 'scripts', 'utils', 'apitypes.js'), 'wb') as f:
        f.write("""// Autogenerated, do not edit!
/*jslint -W070: false*/
define([], function() {
\t'use strict';
\treturn {
""")

    for name in enums:
        enum = getattr(apitypes, name)
        values = dict((attr, getattr(enum, attr))
                      for attr in dir(enum) if not attr.startswith("_"))

        f.write("\t\t{}: {},\n".format(name, values))

    f.write("\t};\n});")
    f.close()


if __name__ == "__main__":
    main()
