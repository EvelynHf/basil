#! /usr/bin/env python
# ______________________________________________________________________
"""Test module test04.my

Give an example of computation at various stages in Python.

Jonathan Riehl

$Id$
"""
# ______________________________________________________________________

def main ():
    mycode = """print 'You should see this at exec time!"""
    print "You should see this at run time!"
    exec mycode

print "You should see this at import time!"

if __name__ == "__main__":
    main()

# ______________________________________________________________________
# End of test04.py
