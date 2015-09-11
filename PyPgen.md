# Introduction #

PyPgen is an implementation of pgen, the Python parser generator, written in Python.  It expects pgen grammar as input, and outputs a Python module that implements a LL(1) parser for the input grammar.

# Details #

## Questions ##

(Please note these questions are hand picked from a pool of hypothetical users, so technically they are neither frequent nor asked.)

### How do I use it? ###

To use PyPgen:
  1. Follow the download and path instructions for using Basil on the GettingStarted page.  PyPgen is written in Python, and should not require one to use the `distutils` build and install (though Basil provides a `setup.py`).
  1. Use the command line interface.

```
$ PyPgen <infile> [-o <outfile>]
```

The "-o" flag is optional, and the results are output

The resulting module defines a parser class.  The parser class is in turn _supposed_ to conform to the parser API proposed in PEP 269.

In the future I want to support more output options (in the code, it looks like it wants to also output C, so I could make it a drop in replacement for the CPython pgen).

### How do I make it a stand alone parser? ###

For any basic Python-like language (where Python-like means that you are using Python's lexical conventions), the default output should be valid Python.  For example:

```
$ PyPgen test.pgen -o test.py
$ chmod +x test.py
$ ./test.py < infile
```

This should pretty print a ConcreteSyntaxTree for the given `infile`.

### What is all that gobbledygook it outputs? ###

PyPgen was originally designed to output something that could be easily handled by RPython (which in 2003 was defined as "stuff we could easily infer a type for").  For that reason PyPgen output avoids both dictionaries and uses classes minimally.  Instead it basically attempt to express the original CPython grammar object using strings, lists, tuples, and integers.

Using my own made up type annotations, the code is sprinkled with documentation about what that stuff actually is.  Here it is in one grand unified chunk of stuff:

```
NFA := [ type : Int, name : String, [ STATE ], start : Int, finish : Int ]
STATE := [ ARC ]
ARC := ( labelIndex : Int, stateIndex : Int )
Grammar := ( [ DFA ], [ Label ], Start : Int , Accel : Int )
DFA := ( Type : Int, Name : String, Initial : Int, [ State ], First : String )
State := ( [ Arc ], Accel, Accept : Int )
Arc := ( Label : Int, StateIndex )
Accel := ( Upper : Int, Lower : Int, [ Int ] )
Label := ( Type : Int, Name : String )
```

The NFA is an intermediate form of an automaton used to parse a particular nonterminal.  This is translated by PyPgen to a DFA, which is packaged into a grammar.

## See Also ##

XXX: There is currently yet another parser generator for MyFront.  Its guts should be put into PyPgen.

XXX: Need stuff to see, also.