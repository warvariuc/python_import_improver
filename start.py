#!/usr/bin/env python3

import sys
import builtins
import traceback
import importlib


def _import(name, globals=None, locals=None, fromlist=None, level=0, __import__=__import__):
    """A hack to make names of imported modules to be available in the parent package before
    they are fully imported. If a module is present in sys.modules event if it's not fully
    imported, it should not be a problem.
    I.e. ``from package import module1, module2`` will create variables ``package.module1`` and
    ``package.module2`` at start of the import, not when it's finished.
    This helps in some situations with circular import.
    """
    if name.startswith('scripts'):
        print('\n__import__(name="%s", fromlist=%s)' % (name, fromlist))
        stack = traceback.format_stack()
        print(''.join(stack))
    module = __import__(name, globals, locals, fromlist, level)
    print('Imported %r' % module)
    for attr in fromlist or ():
        sub_module = sys.modules.get(module.__name__ + '.' + attr)
        if sub_module:  # is this a module?
            # if subpackage is already being imported, even if not finished,
            # inject its name into the parent package
            print('\nInjecting submodule `%s` into module `%s`\n'
                  % (sub_module.__name__, module.__name__))
            setattr(module, attr, sub_module)
    return module

# comment this line to test the old behavior
builtins.__import__ = _import


print('start.py: from scripts import main')
from scripts import main
