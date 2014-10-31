fourpiskytools
==============

A handful of simple convenience functions tying together use of the
[voevent-parse](http://voevent-parse.readthedocs.org/) and 
[Comet](http://comet.transientskp.org/) 
packages, providing a 
quick and easy way to get started sending VOEvents to the 
[4 Pi Sky](http://4pisky.org) 
VOEvent broker (or indeed any VOEvent node of your choice).

This package should be considered 'opinionated', in that it makes some basic
assumptions about what you want to do, in order to make the interface simpler.
Those with more specific requirements should probably refer to this package as
a quick example, and then use *voevent-parse* and *Comet* directly.

Features
--------
* A function provding a *subprocess* wrapper about *comet-sendvo*, to allow
  publishing of [VOEvents](http://en.wikipedia.org/wiki/VOEvent) from a scripted
  process.
* A simple (~3 lines) routine for generating unique identifiers to tag your
  VOEvents with.
* A couple of ready-made functions that take a dictionary defining the sender's 
  'identity' and provide one-liner methods for composing VOEvent packets.

That's it! The package is intentionally minimal.
 

Installation
------------
A [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html)
is recommended, but not essential.
I also recommend use of
[pip](http://pip.readthedocs.org/en/latest/quickstart.html)
since it allows easy version checking and package uninstallation.

Once you've checked out the code, from the package root directory run:

    pip install .
    

Or if you prefer the traditional method:

    python install setup.py


Usage
-----
See the [examples](examples).
