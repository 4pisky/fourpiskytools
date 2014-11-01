#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="fourpiskytools",
    version="0.1.1",
    packages=['fourpiskytools', ],
    description="VOEvent packet generation and transmission using 'voevent-parse' and 'Comet'.",
    author="Tim Staley",
    author_email="timstaley337@gmail.com",
    url="https://github.com/timstaley/fourpiskytools",
    install_requires=required
)
