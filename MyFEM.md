# Introduction #

MyFEM is an embedded domain specific language implemented in Python and embedded in Mython.  MyFEM allows users to embed weak form partial differential equations.  These are used in the FiniteElementMethod, with the current implementation generating C++ that links with the PETSc scientific framework.

# Getting Started #

Here is a basic means of getting started:
  1. Make sure you are using a supported version of Python.
    * Somehow a 2.5-ism got slipped in (a conditional expression in the MyFront compiler code).  Therefore, Python 2.5 or greater is required.
  1. Download the Basil framework.
    * Example: `$ svn co http://basil.googlecode.com/svn/trunk/basil/ basil`
    * See http://code.google.com/p/basil/source/checkout.
  1. Add Basil to your Python path.
    * Example: `$ export PYTHONPATH=${PYTHONPATH}:${PWD}`
    * Note that MyFront is currently in pure Python, and does not require you to build the framework.
  1. Add the Basil application scripts to your path.
    * Example `$ export PATH=${PWD}/basil/apps:${PATH}`
  1. Try running the tests.
    * Examples:
      * `$ ./basil/lang/fenics/tests/fe_test01.my`
      * `$ ./basil/lang/fenics/tests/fe_test02.my`

# Syntax #

FixMe - This is going in a paper that is in preparation.

# Semantics #

FixMe - Same deal as above.

# See Also #

  * http://www.fenics.org/
  * http://www.mcs.anl.gov/petsc