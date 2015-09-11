Here is a basic means of getting started with Mython, the Basil language framework, and the MyFront compiler:
  1. Make sure you are using a supported version of Python.
    * Somehow a 2.5-ism got slipped in (a conditional expression in the MyFront compiler code).  Therefore, Python 2.5 or greater is required.
    * There is a problem using the Python 2.6 tokenizer, so you may be restricted to 2.5.x.  See [issue 8](https://code.google.com/p/basil/issues/detail?id=8).
  1. Download the Basil framework.
    * Example: `$ svn co http://basil.googlecode.com/svn/trunk/basil/ basil`
    * See http://code.google.com/p/basil/source/checkout.
  1. Add Basil to your Python path.
    * Example: `$ export PYTHONPATH=${PYTHONPATH}:${PWD}`
    * Note that MyFront is currently in pure Python, and does not require you to build the framework.
  1. Add the Basil application scripts to your path.
    * Example `$ export PATH=${PWD}/basil/apps:${PATH}`
  1. Try it out.
    * There are some test Mython scripts in `.../basil/lang/mython/tests/`.
    * For example, `test04.my`, gives an example of the various evaluation stages that MyFront.  Try both ways of running it:
      * `.\test04.my`
        * This uses the `mython` wrapper script.
      * Or, `MyFront test04.my` and then `python -m test04`
        * This uses MyFront to build a `test04.pyc` file, and then runs it using Python.