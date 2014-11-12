#!/bin/sh

# Create a new, empty virtualenv

virtualenv 4pstools_venv
# Activate it
. 4pstools_venv/bin/activate
# and install this package into it...
pip install .

