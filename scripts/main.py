import sys


print("""
This is module `scripts.main` (scripts/main.py). It is being imported.

Its parent module package `scripts` has already been imported:
sys.modules["scripts"] == %r

Module `scripts` does not yet have attribute `main`. It will be there when this module
(`scripts.main`) finishes loading:
getattr(sys.modules["scripts"], "main", None) == %r

But module `scripts.main` has already been created:
sys.modules["scripts.main"] == %r

""" % (
    sys.modules["scripts"],
    getattr(sys.modules["scripts"], "main", None),
    sys.modules["scripts.main"],
))

print('scripts/main.py: from . import install')
from . import install
