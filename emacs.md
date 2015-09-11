# Introduction #

Mython's additional construct, quote blocks, are currently have rudimentary support with this emacs mode.


# Details #

mython-mode.el, which is derived from python-mode.el, is located in /sandbox

To install:

Add these to your .emacs file:

(add-to-list 'load-path "

&lt;mython-path&gt;

/sandbox")
(require 'mython-mode)
(push '("\\.my\\'" . mython-mode)
> auto-mode-alist)

Make sure to put a space after quote keyword, like so,

quote [myfrontend](myfrontend.md) module1:

in order to get the syntax highlighting and indentation benefits this mode offers.