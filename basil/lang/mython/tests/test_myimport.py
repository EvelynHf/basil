#! /usr/bin/env python
# ______________________________________________________________________
"""test_myimport.py

Implements unit tests for the basil.lang.mython.myimport module.

Jonathan Riehl
"""
# ______________________________________________________________________
# Module imports

import os
import sys
import unittest
import StringIO

from basil.lang.mython import myimport

# ______________________________________________________________________
# Class definitions

class TestMyImport (unittest.TestCase):
    """Unit test the basil.lang.mython.myimport.MythonImporter class,
    and its hooks."""
    def _make_sure_test04_does_not_exist (self):
        testdir, _ = os.path.split(__file__)
        test_pyc = os.path.join(testdir, "test04.pyc")
        if __debug__:
            sys.stderr.write(str(test_pyc) + "\n")
        if os.path.exists(test_pyc):
            print("Removing %r" % test_pyc)
            os.remove(test_pyc)
            if __debug__:
                sys.stderr.write(str(os.path.exists(test_pyc)) + "\n")

    def _import_test04 (self):
        self._make_sure_test04_does_not_exist()
        from basil.lang.mython.tests import test04
        return test04

    def test_import_hook (self):
        myimporter = myimport.MythonImporter
        # Other tests may install the import hook, so make sure it isn't there.
        if myimporter in sys.meta_path:
            if __debug__:
                sys.stderr.write("\n\nWarning in test_import_hook(): the "
                                 "MythonImporter hook is already installed.  "
                                 "Uninstalling.\n\n")
            sys.meta_path.remove(myimporter)
        self.assert_(myimporter not in sys.meta_path)
        self.failUnlessRaises(ImportError, self._import_test04)
        myimport.install_import_hook()
        self.assert_(myimporter in sys.meta_path)
        stdout = sys.stdout
        txtbuf = StringIO.StringIO()
        sys.stdout = txtbuf
        self.assert_(self._import_test04())
        sys.stdout = stdout
        test_output = txtbuf.getvalue()
        is_compiling = "compile" in test_output
        if __debug__:
            print(test_output)
        self.assert_(is_compiling)
        sys.meta_path.remove(myimporter)
        self.assert_(myimporter not in sys.meta_path)

    # TODO: Write a test that ensures that the mtime logic works
    # (properly recompiles when the .my file is newer than the .pyc).

# ______________________________________________________________________
# Main (test) routine

if __name__ == "__main__":
    unittest.main()

# ______________________________________________________________________
# End of test_myimport.py
