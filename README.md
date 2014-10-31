
fourpiskytools
==============

A thin wrapper over the 
[voevent-parse](http://voevent-parse.readthedocs.org/) and 
[Comet](http://comet.transientskp.org/) 
packages, providing a 
quick and easy way to get started sending VOEvents to the 
[4 Pi Sky](http://4pisky.org) 
VOEvent broker (or indeed any VOEvent node of your choice).

This package should be considered 'opinionated', in that it makes some basic
assumptions about what you want to do, in order to make the interface simpler.
Those with more specific requirements should probably refer to this package as
a quick example, and then use 'voevent-parse' and 'Comet' directly.

Installation
------------
A virtualenv is recommended, but not essential. A simple:

    pip install .

should do the trick, pulling in requirements as needed. 

Usage
-----
See the [examples](examples).
