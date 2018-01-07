#!/usr/bin/env python
"""A small wrapper around pytest.
"""
import sys
import pytest

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(pytest.main())

