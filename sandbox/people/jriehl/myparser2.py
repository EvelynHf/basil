#! /usr/bin/env python
# ______________________________________________________________________
# Module imports

import os
import StringIO

from basil.parsing import PgenParser, PyPgen, nfa, trampoline
import basil.lang.python
from basil.lang.python import DFAParser
import mylexer2

# ______________________________________________________________________
# Module data

MY_GRAMMAR_EXT2="""
not_expr: BANG ['[' expr ']'] myexpr
compound_stmt: 'mydef' ['[' expr ']'] [NAME [parameters]] mysuite
mysuite: ':' (MYSUITE NEWLINE | NEWLINE MYSUITE)
myexpr: '(' MYEXPR ')'
"""

pgen = PyPgen.PyPgen()

py_grammar_path = os.path.split(basil.lang.python.__file__)[0]

TEST_STRINGS=[
"""mydef[namedtupledef] Point(x, y): pass
"""

# ______________________________________________________________________
# Function definition(s)

def pgen_compose (pgen_st1, pgen_st2, start_symbol, additional_tokens = None):
    nfa_grammar1 = pgen.handleStart(pgen_st1)
    nfa_grammar2 = pgen.handleStart(pgen_st2)
    nfa_composed = nfa.compose_nfas(nfa_grammar1, nfa_grammar2)
    grammar3 = pgen.generateDfaGrammar(nfa_composed, start_symbol)
    pgen.translateLabels(grammar3, additional_tokens)
    pgen.generateFirstSets(grammar3)
    grammar3[0] = map(tuple, grammar3[0])
    return DFAParser.addAccelerators(tuple(grammar3))

# ______________________________________________________________________
# Class definition(s)

class MyParser2 (object):
    py_pgen_st = PgenParser.parseFile(os.path.join(py_grammar_path,
                                                   'python26/Grammar'))
    my_ext_pgen_st = PgenParser.parseString(MY_GRAMMAR_EXT2)
    my_grammar = pgen_compose(py_pgen_st, my_ext_pgen_st, 'file_input',
                              { 'BANG' : mylexer2.BANG,
                                'MYEXPR' : mylexer2.MYEXPR,
                                'MYSUITE' : mylexer2.MYSUITE })

# ______________________________________________________________________
# Main (self-test) routine

def main (*args):
    pass

# ______________________________________________________________________

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])

# ______________________________________________________________________
# End of myparser2.py
