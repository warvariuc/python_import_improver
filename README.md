Python import improver
======================

A hack to make names of imported modules to be available in the parent package before they are fully imported. 

If a module is present in ``sys.modules`` event if it hasn't been fully imported, it should not be a problem.

I.e. ``from package import module1, module2`` will create variables ``package.module1`` and ``package.module2`` at start of the import, not when it's finished.

This helps in some situations with circular import.
