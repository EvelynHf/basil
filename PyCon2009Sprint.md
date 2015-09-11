# Introduction #

The primary focus of this sprint is preparing Mython for a public release.  Our primary goals are:
  * Write a set of tutorials that demonstrate and motivate use of the MyFront compiler and other Basil tools.
  * Make syntax error reporting sane.

Our secondary goals are to start hardening the code base for public consumption.  Working towards this goal can include adding tests, identifying and automating existing tests, writing documentation, project planning, establishing and rewriting code to a coding standard, and improving the uniformity of the various API's in the BasilFramework.

# Sunday, March 29, 2009 #

I ([Jon](http://code.google.com/u/jon.riehl/)) gave a kick off talk that attempted to explain the scope and goals of the project.  Here is an outline of the notes I used:
  * What is [Mython](Mython.md)?
    * An extensible variant of Python.
    * Adds CompileTimeMetaprogramming to the Python language.
      * Syntax marks certain blocks of code as compile-time expressions.
      * These blocks of code are evaluated at compile-time, generating run-time code in the form of PythonAbstractSyntax.
  * What is MyFront?
    * The initial implementation of the [Mython](Mython.md) language.
    * Compiles [Mython](Mython.md) source to PythonBytecode.
    * An OpenCompiler - the parts of the compiler, including the tools used to build it, are reflected to the compile-time evaluation environment.
  * What is the BasilFramework?
    * A framework for developing languages in Python.
    * Goal is to provide glue for composing the products of the wide variety of language development tools out there.
    * Seeking to make this the "standard library" for [Mython](Mython.md).

Some terminology I use:
  * What is an integration?
    * Ideally, an integration is a pair of transformers.
    * The first transformer maps from some source representation (either text or some structure intermediate representation) to a target representation (usually a tree, graph, or directed-acyclic graph).
      * In many cases, this is just a _parser_.
    * The second transformer maps from the target representation back to the source representation.
      * In many cases, this is just a _pretty printer_.
    * Given integration (T, T-1), for all s in source representation, T(T-1(T(s))) == T(s) should hold.
    * In modeling circles this is also called round trip engineering.
  * A _parser generator integration_ is an integration from the source code of a parser generator to the BasilGrammarModel, and back again.
  * A _language integration_ is an integration from the source code of a language to some intermediate representation, and back again.
  * A _staging language integration_ is an integration from the source code of a language to PythonAbstractSyntax that, when evaluated, builds an intermediate representation specific to that language.
    * These kinds of integrations are important for building front ends in MyFront.

What are the applications in the BasilFramework, and how do they demonstrate the ideas presented above?
  * [Grammarian](Grammarian.md)
  * PyPgen - This is a pure Python implementation of the `pgen` tool.
    * **TODO**
  * [asdl\_py](asdl_py.md) - This is an adaptation of the `asdl_c.py` tool in Python.
    * **TODO**
  * MyFront - This uses a (broken, incorrect, but useful for my purposes) variant of PyPgen and some other utilities to create a compiler.  As mentioned above, staging language integrations can quickly define useful QuotationFunctions.

(Not mentioned, because of rampant contradictions in the code base) Coding philosophy:
  * Try to avoid reinvention of the wheel (but constant reinvention of the axle is okay).
  * Embrace and extend.
  * There is no one true intermediate representation (though I've recently been using [ASDL](ASDL.md) pretty heavily).
    * Would like to host a marketplace of intermediate representations.
      * (See n-languages slide in http://people.cs.uchicago.edu/~jriehl/Grammatech.pdf.)

Implementation backbone:
  * Trees
    * Tend to heavily use a nesting of tuples and lists:
      * `tree := ( payload, [ tree* ] )`
  * Visitors
    * I tend to call them "handlers".

Ideas for the job jar:
  * Familiarize attendees with [Mython](Mython.md).
  * Build new (little) language integrations.
  * Bugs (esp. error reporting)
  * Code review and rewriting:
    * Adopt a coding standard and start making the code conform to the standard.
      * Thinking of PEP-8.
  * Adopt a test automation framework, and start identifying and plugging-in existing tests.
  * Documentation
  * Rewrites (AbstractSyntaxRewriteLanguage)
  * Back-end support plan.
    * Code?  PyCUDA, CorePy, LLVM?
  * Port to Python 3000?

# Monday, March 30, 2009 #

Today, I'd like to do something like this:

```
#! /usr/bin/env mython

from somewhere import pgen

quote [pgen] myparser:
    start: stmt*
    stmt: (ID '=' expr) | ('print' ID)
    expr: term ('*' expr)*
    ...

quote [myfront] mytranslator:
    ...

quote [mytranslator] mycode:
    a = 2
    print a

print mycode
exec mycode

```

Adding support code as we go, then documenting it as a tutorial.

Then maybe we inject syntax errors, and try to figure out how to make the reports for the error more useful and readable.

Report:
  * SUCCESS!!1! - `.../sandbox/pycon2009/demo.my`
  * (Up against a very annoying fail - see http://code.google.com/p/basil/issues/detail?id=10)
  * More things to do (from whiteboard at end of day):
    * Rewrite `MyFront`.
      * Front-end for 2.6
      * Front-end for 3.0
      * Front-end for 3.1
      * Get rid of `pgen2LL1.py`
      * Improve error handling in quote expander
      * Fix the bytecode generator (see issue above)
    * Basil language integrations
      1. Define a uniform API to language integrations.
      1. Get test strings.
        * Meet "language integration condition": `parse(prettyprint(parse(source))) == parse(source)`.
      1. Set up test framework.
      1. Get all
    * Parser generator integrations
      * `ply`

# Tuesday, March 31, 2009 #

We did the following:
  * Andy added some preliminary support for Sphinx, which can build our documentation ([issue 11](https://code.google.com/p/basil/issues/detail?id=11)).
  * Chris started working on a port to Python 2.6 ([issue 8](https://code.google.com/p/basil/issues/detail?id=8)).
  * Tyler and I did a bit of prototyping:
    * We wrote another calculator demo, but used PLY to generate the parser this time.
    * We started work on a pretty-printer for Mython.
  * Tyler also got started prototyping a `ply` parser integration.
  * I came up with a fix for [issue 9](https://code.google.com/p/basil/issues/detail?id=9). (http://code.google.com/p/basil/issues/detail?id=9)
  * I found, and tried to fix [issue 12](https://code.google.com/p/basil/issues/detail?id=12).  (http://code.google.com/p/basil/issues/detail?id=12)

# Wednesday, April 1, 2009 #

## Grammarian ##

While discussing things at the start of the day, Jon (who is now apparently switching to third person) showed Tyler [Grammarian](Grammarian.md).  Unfortunately, some hacking a couple months ago (trying to build a GUI front-end to [Grammarian](Grammarian.md)) broke the command-line application.

Jon fixed this and checked it into [r69](https://code.google.com/p/basil/source/detail?r=69).  He then expanded Tyler's experiment with a PLY integration, adding rudimentary model generation.  The result now outputs an XML document that conforms to the BasilGrammarModel DTD.  (See [r70](https://code.google.com/p/basil/source/detail?r=70) version of `.../sandbox/pycon2009/ply_integrator.py`.)

We'll need to rewrite the modeling aspects of [Grammarian](Grammarian.md).  It's heavy reliance on factories is overkill (though if we want to build HashCons style stuff, we'd have to use metaclasses, IIUC).

## SPARK ##

Tyler wrote a SPARK based calculator. He ran into some problems, and Jon helped out.  By the end of the day they resolved these problems (though neither of them really understands what the problem was - it had something to do with a set membership test failing on line 328 of `.../basil/thirdparty/spark.py`; IIRC, adding a cmp operation fixed this).

You can look at the demo here: `.../sandbox/pycon2009/spark_calc.my`

# Thursday, April 2, 2009 #

## Error Reporting ##

Jon worked on improving error reporting in the `MyFront` and `mython` applications.  Tests that demonstrate his work:
  * `.../basil/lang/mython/tests/test08.my`
  * `.../sandbox/pycon2008/syntax-error.my`
  * `.../sandbox/pycon2008/syntax-error-2.my`

This work isn't sufficient to resolve [issue 3](https://code.google.com/p/basil/issues/detail?id=3).  See comments added to `.../basil/lang/mython/MyFrontUtils.py`.

## Demo Extensions ##

Tyler added variables and assignment to the PLY calculator demo, as well as an evaluator that handles these properly.

## Rewriting ##

Tyler and Jon did some pair programming on code that builds an optimizing rewriter for the calculator demo intermediate representation.

See: `.../sandbox/pycon2009/rwdemo.my`

# Summary #

I think the sprint went well.  We now have demonstrations of using several Python-based parser generators to build quotation functions.  We've found and resolved several defects, and broken ground on usability improvements to the compiler.  I'm looking forward to writing more of this up, and showing people what we have to offer.  Thanks to all who participated!  -Jon