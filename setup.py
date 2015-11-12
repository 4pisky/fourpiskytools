#!/usr/bin/env python

from setuptools import setup

install_requires = [
    "comet>=1.1.0",
    "voevent-parse>=0.7.0",
]


## Optional: allows nice 'desktop notifications' on Ubuntu-like systems
## BUT: Requires GOBject, probably more trouble than it's worth on e.g. Mac OSX.
extras_require = {
    'pgi': ['pgi'],
}

setup(
    name="fourpiskytools",
    version="0.2.0",
    packages=['fourpiskytools', ],
    description="VOEvent packet generation and transmission using 'voevent-parse' and 'Comet'.",
    author="Tim Staley",
    author_email="timstaley337@gmail.com",
    url="https://github.com/timstaley/fourpiskytools",
    install_requires=install_requires,
    extras_require=extras_require,
)
