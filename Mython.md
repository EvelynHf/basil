# Introduction #

Mython is an extensible Python variant.  A compiler for Mython, MyFront, is available as a part of the Basil framework.  The Mython language adds a quotation mechanism that allows users to:
  * Stage code for later evaluation, embedding an abstract syntax tree as a value in the resulting bytecode.  The staging mechanism is extensible by virtue of allowing an arbitrary parsing function to be used.
  * Escape into the compiler, changing language properties at compile time, and introducing new parsing functions for later quotation.

# Details #

**FIXME**